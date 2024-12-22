CREATE INDEX ClusteredIX_Ksiazka ON Ksiazka (Ksiazka_ID, Tytul ASC);
CLUSTER Ksiazka USING ClusteredIX_Ksiazka;

EXPLAIN ANALYZE
SELECT Ksiazka_ID, Tytul
FROM Ksiazka
ORDER BY Tytul ASC
LIMIT 10;


--------------------------------------------------------------------------------------------------------------------------------------------
--  Limit  (cost=22504.71..22505.88 rows=10 width=37) (actual time=27.000..27.896 rows=10 loops=1)
--    ->  Gather Merge  (cost=22504.71..119733.80 rows=833334 width=37) (actual time=26.999..27.895 rows=10 loops=1)
--          Workers Planned: 2
--          Workers Launched: 2
--          ->  Sort  (cost=21504.69..22546.36 rows=416667 width=37) (actual time=25.609..25.610 rows=8 loops=3)
--                Sort Key: tytul
--                Sort Method: top-N heapsort  Memory: 26kB
--                Worker 0:  Sort Method: top-N heapsort  Memory: 26kB
--                Worker 1:  Sort Method: top-N heapsort  Memory: 26kB
--                ->  Parallel Seq Scan on ksiazka  (cost=0.00..12500.67 rows=416667 width=37) (actual time=0.021..14.124 rows=333333 loops=3)
--  Planning Time: 0.157 ms
--  Execution Time: 27.904 ms
-- (12 rows)

--------------------------------------------------------------------------------------------------------------------------------------------
-- bez:
--  Limit  (cost=22504.71..22505.88 rows=10 width=37) (actual time=67.396..68.612 rows=10 loops=1)
--    ->  Gather Merge  (cost=22504.71..119733.80 rows=833334 width=37) (actual time=67.394..68.608 rows=10 loops=1)
--          Workers Planned: 2
--          Workers Launched: 2
--          ->  Sort  (cost=21504.69..22546.36 rows=416667 width=37) (actual time=62.645..62.645 rows=7 loops=3)
--                Sort Key: tytul
--                Sort Method: top-N heapsort  Memory: 26kB
--                Worker 0:  Sort Method: top-N heapsort  Memory: 26kB
--                Worker 1:  Sort Method: top-N heapsort  Memory: 26kB
--                ->  Parallel Seq Scan on ksiazka  (cost=0.00..12500.67 rows=416667 width=37) (actual time=0.060..34.794 rows=333333 loops=3)
--  Planning Time: 0.446 ms
--  Execution Time: 68.638 ms
-- (12 rows)


DROP INDEX IF EXISTS ClusteredIX_Ksiazka;

CREATE INDEX NonClusteredIX_Egzemplarz ON Egzemplarz (Egzemplarz_ID, Ksiazka_ID);

EXPLAIN ANALYZE
SELECT Egzemplarz_ID, Ksiazka_ID
FROM Egzemplarz
LIMIT 10;

---------------------------------------------------------------------------------------------------------------------
--  Limit  (cost=0.00..0.14 rows=10 width=8) (actual time=0.057..0.059 rows=10 loops=1)
--    ->  Seq Scan on egzemplarz  (cost=0.00..72124.00 rows=5000000 width=8) (actual time=0.055..0.056 rows=10 loops=1)
--  Planning Time: 0.625 ms
--  Execution Time: 0.075 ms
-- (4 rows)
-----------------------------------
-- bez:
--  Limit  (cost=0.00..0.14 rows=10 width=8) (actual time=0.019..0.021 rows=10 loops=1)
--    ->  Seq Scan on egzemplarz  (cost=0.00..72124.00 rows=5000000 width=8) (actual time=0.016..0.018 rows=10 loops=1)
--  Planning Time: 0.115 ms
--  Execution Time: 0.038 ms
-- (4 rows)

DROP INDEX IF EXISTS NonClusteredIX_Egzemplarz;

CREATE INDEX IX_Egzemplarz_Ksiazka_ID ON Egzemplarz (Ksiazka_ID);
CREATE INDEX IX_Ksiazka_ID ON Ksiazka (Ksiazka_ID);

-- Analyze query with join
EXPLAIN ANALYZE
SELECT * 
FROM Ksiazka 
JOIN Egzemplarz ON Ksiazka.Ksiazka_ID = Egzemplarz.Ksiazka_ID
LIMIT 10;

--  Limit  (cost=0.43..1.90 rows=10 width=45) (actual time=0.007..0.014 rows=10 loops=1)
--    ->  Nested Loop  (cost=0.43..733134.00 rows=5000000 width=45) (actual time=0.006..0.013 rows=10 loops=1)
--          ->  Seq Scan on ksiazka  (cost=0.00..18334.00 rows=1000000 width=37) (actual time=0.003..0.003 rows=2 loops=1)
--          ->  Index Scan using ix_egzemplarz_ksiazka_id on egzemplarz  (cost=0.43..0.65 rows=6 width=8) (actual time=0.002..0.004 rows=5 loops=2)
--                Index Cond: (ksiazka_id = ksiazka.ksiazka_id)
--  Planning Time: 0.330 ms
--  Execution Time: 0.023 ms
-- (7 rows)
-------------------------------------------------------------------
-- bez:
--  Limit  (cost=0.42..5.08 rows=10 width=45) (actual time=0.039..0.157 rows=10 loops=1)
--    ->  Nested Loop  (cost=0.42..2328939.87 rows=5000000 width=45) (actual time=0.037..0.154 rows=10 loops=1)
--          ->  Seq Scan on egzemplarz  (cost=0.00..72124.00 rows=5000000 width=8) (actual time=0.014..0.015 rows=10 loops=1)
--          ->  Index Scan using ksiazka_pkey on ksiazka  (cost=0.42..0.45 rows=1 width=37) (actual time=0.013..0.013 rows=1 loops=10)
--                Index Cond: (ksiazka_id = egzemplarz.ksiazka_id)
--  Planning Time: 0.464 ms
--  Execution Time: 0.186 ms
-- (7 rows)


DROP INDEX IF EXISTS IX_Egzemplarz_Ksiazka_ID;
DROP INDEX IF EXISTS IX_Ksiazka_ID;
