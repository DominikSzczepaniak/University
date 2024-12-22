CREATE TABLE Ksiazka (
    Ksiazka_ID SERIAL PRIMARY KEY,
    Tytul VARCHAR(255) NOT NULL
);

CREATE TABLE Egzemplarz (
    Egzemplarz_ID SERIAL PRIMARY KEY,
    Ksiazka_ID INT NOT NULL,
    FOREIGN KEY (Ksiazka_ID) REFERENCES Ksiazka(Ksiazka_ID)
);

CREATE TABLE Czytelnik (
    Czytelnik_ID SERIAL PRIMARY KEY,
    PESEL VARCHAR(11) NOT NULL,
    Nazwisko VARCHAR(255) NOT NULL
);

CREATE TABLE Wypozyczenie (
    Wypozyczenie_ID SERIAL PRIMARY KEY,  
    Egzemplarz_ID INT NOT NULL,
    Czytelnik_ID INT NOT NULL,
    FOREIGN KEY (Egzemplarz_ID) REFERENCES Egzemplarz(Egzemplarz_ID),
    FOREIGN KEY (Czytelnik_ID) REFERENCES Czytelnik(Czytelnik_ID)
);

INSERT INTO Ksiazka (Ksiazka_ID, Tytul) 
SELECT generate_series(1, 1000000), md5(random()::text);

INSERT INTO Egzemplarz (Egzemplarz_ID, Ksiazka_ID)
SELECT generate_series(1, 5000000), floor(random() * 1000000) + 1;

INSERT INTO Czytelnik (Czytelnik_ID, PESEL, Nazwisko)
SELECT generate_series(1, 2000000), '11111111111', md5(random()::text);

INSERT INTO Wypozyczenie (Wypozyczenie_ID, Egzemplarz_ID, Czytelnik_ID)
SELECT generate_series(1, 10000000), floor(random() * 5000000) + 1, floor(random() * 2000000) + 1;

-- Query 1 Sequential scans or index scans on the involved tables, followed by joins optimized by leveraging indexes for join conditions
EXPLAIN ANALYZE
SELECT DISTINCT c.PESEL, c.Nazwisko
FROM Egzemplarz e
JOIN Ksiazka k ON e.Ksiazka_ID=k.Ksiazka_ID
JOIN Wypozyczenie w ON e.Egzemplarz_ID=w.Egzemplarz_ID
JOIN Czytelnik c ON c.Czytelnik_ID = w.Czytelnik_ID;

------------------------------------------------------------------------------------------------------------------------------------------------------
--  HashAggregate  (cost=1877673.68..2091511.53 rows=2000000 width=45) (actual time=9115.820..10314.280 rows=1986490 loops=1)
--    Group Key: c.pesel, c.nazwisko
--    Planned Partitions: 128  Batches: 129  Memory Usage: 4625kB  Disk Usage: 646936kB
--    ->  Hash Join  (cost=274048.00..826641.77 rows=11027220 width=45) (actual time=1383.872..7504.831 rows=10000000 loops=1)
--          Hash Cond: (w.czytelnik_id = c.czytelnik_id)
--          ->  Hash Join  (cost=188897.00..606860.25 rows=11027220 width=4) (actual time=894.142..5140.305 rows=10000000 loops=1)
--                Hash Cond: (e.ksiazka_id = k.ksiazka_id)
--                ->  Hash Join  (cost=154156.00..453113.67 rows=11027220 width=8) (actual time=636.199..3351.636 rows=10000000 loops=1)
--                      Hash Cond: (w.egzemplarz_id = e.egzemplarz_id)
--                      ->  Seq Scan on wypozyczenie w  (cost=0.00..164327.20 rows=11027220 width=8) (actual time=0.044..655.716 rows=10000000 loops=1)
--                      ->  Hash  (cost=72124.00..72124.00 rows=5000000 width=8) (actual time=582.738..582.739 rows=5000000 loops=1)
--                            Buckets: 131072  Batches: 128  Memory Usage: 2553kB
--                            ->  Seq Scan on egzemplarz e  (cost=0.00..72124.00 rows=5000000 width=8) (actual time=0.014..235.456 rows=5000000 loops=1)
--                ->  Hash  (cost=18334.00..18334.00 rows=1000000 width=4) (actual time=137.554..137.554 rows=1000000 loops=1)
--                      Buckets: 131072  Batches: 16  Memory Usage: 3227kB
--                      ->  Seq Scan on ksiazka k  (cost=0.00..18334.00 rows=1000000 width=4) (actual time=0.764..70.165 rows=1000000 loops=1)
--          ->  Hash  (cost=40619.00..40619.00 rows=2000000 width=49) (actual time=406.022..406.023 rows=2000000 loops=1)
--                Buckets: 65536  Batches: 64  Memory Usage: 3078kB
--                ->  Seq Scan on czytelnik c  (cost=0.00..40619.00 rows=2000000 width=49) (actual time=0.036..140.402 rows=2000000 loops=1)
--  Planning Time: 4.548 ms
--  Execution Time: 10983.498 ms
-- (21 rows)

-- Query 2 Exercutes the subquery, stores the result in memory then performs filter. Could be less efficient if the subquery is not optimized.
EXPLAIN ANALYZE
SELECT c.PESEL, c.Nazwisko
FROM Czytelnik c WHERE c.Czytelnik_ID IN
(SELECT w.Czytelnik_ID FROM Wypozyczenie w
JOIN Egzemplarz e ON e.Egzemplarz_ID=w.Egzemplarz_ID
JOIN Ksiazka k ON e.Ksiazka_ID=k.Ksiazka_ID);

------------------------------------------------------------------------------------------------------------------------------------------------------
--  Nested Loop  (cost=634428.73..635842.72 rows=1000000 width=45) (actual time=5914.853..13011.082 rows=1986490 loops=1)
--    ->  HashAggregate  (cost=634428.30..634430.30 rows=200 width=4) (actual time=5914.833..7576.727 rows=1986490 loops=1)
--          Group Key: w.czytelnik_id
--          Batches: 85  Memory Usage: 4265kB  Disk Usage: 241152kB
--          ->  Hash Join  (cost=188897.00..606860.25 rows=11027220 width=4) (actual time=627.689..4856.473 rows=10000000 loops=1)
--                Hash Cond: (e.ksiazka_id = k.ksiazka_id)
--                ->  Hash Join  (cost=154156.00..453113.67 rows=11027220 width=8) (actual time=461.833..2962.534 rows=10000000 loops=1)
--                      Hash Cond: (w.egzemplarz_id = e.egzemplarz_id)
--                      ->  Seq Scan on wypozyczenie w  (cost=0.00..164327.20 rows=11027220 width=8) (actual time=0.012..479.468 rows=10000000 loops=1)
--                      ->  Hash  (cost=72124.00..72124.00 rows=5000000 width=8) (actual time=459.405..459.405 rows=5000000 loops=1)
--                            Buckets: 131072  Batches: 128  Memory Usage: 2553kB
--                            ->  Seq Scan on egzemplarz e  (cost=0.00..72124.00 rows=5000000 width=8) (actual time=0.006..154.096 rows=5000000 loops=1)
--                ->  Hash  (cost=18334.00..18334.00 rows=1000000 width=4) (actual time=157.767..157.767 rows=1000000 loops=1)
--                      Buckets: 131072  Batches: 16  Memory Usage: 3227kB
--                      ->  Seq Scan on ksiazka k  (cost=0.00..18334.00 rows=1000000 width=4) (actual time=0.365..63.703 rows=1000000 loops=1)
--    ->  Index Scan using czytelnik_pkey on czytelnik c  (cost=0.43..8.38 rows=1 width=49) (actual time=0.003..0.003 rows=1 loops=1986490)
--          Index Cond: (czytelnik_id = w.czytelnik_id)
--  Planning Time: 2.225 ms
--  Execution Time: 13083.526 ms
-- (19 rows)


-- Query 3 Sequential evaluation of nested subqueries, with temporary data storage at each level.
EXPLAIN ANALYZE
SELECT c.PESEL, c.Nazwisko
FROM Czytelnik c
WHERE c.Czytelnik_ID IN (
    SELECT w.Czytelnik_ID
    FROM Wypozyczenie w
    WHERE w.Egzemplarz_ID IN (
        SELECT e.Egzemplarz_ID
        FROM Egzemplarz e
        WHERE e.Ksiazka_ID IN (
            SELECT k.Ksiazka_ID
            FROM Ksiazka k
        )
    )
);

-- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
--  Gather  (cost=388127.52..646802.91 rows=1863428 width=45) (actual time=2559.139..3255.781 rows=1986490 loops=1)
--    Workers Planned: 2
--    Workers Launched: 2
--    ->  Parallel Hash Semi Join  (cost=387127.52..459460.11 rows=776428 width=45) (actual time=2546.843..2824.818 rows=662163 loops=3)
--          Hash Cond: (c.czytelnik_id = w.czytelnik_id)
--          ->  Parallel Seq Scan on czytelnik c  (cost=0.00..28952.33 rows=833333 width=49) (actual time=0.027..46.590 rows=666667 loops=3)
--          ->  Parallel Hash  (cost=318766.27..318766.27 rows=4166740 width=4) (actual time=2244.404..2244.411 rows=3333333 loops=3)
--                Buckets: 131072  Batches: 256  Memory Usage: 2624kB
--                ->  Parallel Hash Semi Join  (cost=119849.77..318766.27 rows=4166740 width=4) (actual time=1301.234..1787.183 rows=3333333 loops=3)
--                      Hash Cond: (w.egzemplarz_id = e.egzemplarz_id)
--                      ->  Parallel Seq Scan on wypozyczenie w  (cost=0.00..95722.40 rows=4166740 width=8) (actual time=0.085..189.062 rows=3333333 loops=3)
--                      ->  Parallel Hash  (cost=85669.11..85669.11 rows=2083333 width=4) (actual time=706.718..706.722 rows=1666667 loops=3)
--                            Buckets: 131072  Batches: 128  Memory Usage: 2592kB
--                            ->  Parallel Hash Join  (cost=19337.00..85669.11 rows=2083333 width=4) (actual time=313.620..541.070 rows=1666667 loops=3)
--                                  Hash Cond: (e.ksiazka_id = k.ksiazka_id)
--                                  ->  Parallel Seq Scan on egzemplarz e  (cost=0.00..42957.33 rows=2083333 width=8) (actual time=0.082..81.267 rows=1666667 loops=3)
--                                  ->  Parallel Hash  (cost=12500.67..12500.67 rows=416667 width=4) (actual time=76.541..76.541 rows=333333 loops=3)
--                                        Buckets: 131072  Batches: 16  Memory Usage: 3520kB
--                                        ->  Parallel Seq Scan on ksiazka k  (cost=0.00..12500.67 rows=416667 width=4) (actual time=0.075..29.385 rows=333333 loops=3)
--  Planning Time: 4.029 ms
--  Execution Time: 3294.919 ms
-- (21 rows)
