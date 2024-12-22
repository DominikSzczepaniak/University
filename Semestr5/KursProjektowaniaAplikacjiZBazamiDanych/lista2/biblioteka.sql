USE Test;
GO

DROP TABLE IF EXISTS Wypozyczenie;
GO

DROP TABLE IF EXISTS Egzemplarz;
GO

DROP TABLE IF EXISTS Czytelnik;
GO

DROP TABLE IF EXISTS Ksiazka;
GO

CREATE TABLE Ksiazka
( Ksiazka_ID INT IDENTITY
, ISBN VARCHAR(20)
, Tytul VARCHAR(300)
, Autor VARCHAR(200)
, Rok_Wydania INT
, Cena DECIMAL(10,2)
, Wypozyczona_Ostatni_Miesiac BIT
, CONSTRAINT Ksiazka_PK PRIMARY KEY (Ksiazka_ID)
, CONSTRAINT Ksiazka_UK_ISBN UNIQUE (ISBN)
);
GO

CREATE TABLE Egzemplarz
( Egzemplarz_ID INT IDENTITY
, Sygnatura CHAR(8)
, Ksiazka_ID INT
, CONSTRAINT Egzemplarz_PK PRIMARY KEY (Egzemplarz_ID)
, CONSTRAINT Egzemplarz_UK_Sygnatura UNIQUE (Sygnatura)
, CONSTRAINT Egzemplarz_FK FOREIGN KEY (Ksiazka_ID) REFERENCES Ksiazka (Ksiazka_ID) ON DELETE CASCADE
);
GO

CREATE TABLE Czytelnik
( Czytelnik_ID INT IDENTITY
, PESEL CHAR(11)
, Nazwisko VARCHAR(30)
, Miasto VARCHAR(30)
, Data_Urodzenia DATE
, Ostatnie_Wypozyczenie DATE
, CONSTRAINT Czytelnik_PK PRIMARY KEY (Czytelnik_ID)
, CONSTRAINT Czytelnik_UK_PESEL UNIQUE (PESEL)
);
GO

CREATE TABLE Wypozyczenie
( Wypozyczenie_ID INT IDENTITY
, Czytelnik_ID INT
, Egzemplarz_ID INT
, Data DATE
, Liczba_Dni INT
, CONSTRAINT Wypozyczenie_PK PRIMARY KEY (Wypozyczenie_ID)
, CONSTRAINT Wypozyczenie_FK_Czytelnik FOREIGN KEY (Czytelnik_ID) REFERENCES Czytelnik (Czytelnik_ID) ON DELETE CASCADE
, CONSTRAINT Wypozyczenie_FK_Egzemplarz FOREIGN KEY (Egzemplarz_ID) REFERENCES Egzemplarz (Egzemplarz_ID) ON DELETE CASCADE
);
GO

SET IDENTITY_INSERT Ksiazka ON
INSERT INTO Ksiazka (Ksiazka_ID,ISBN,Tytul,Autor,Rok_Wydania,Cena) VALUES
(1,'83-246-0279-8','Microsoft Access. Podr�cznik administratora','Helen Feddema',2006,69),
(2,'83-246-0653-X','SQL Server 2005. Programowanie. Od podstaw','Robert Vieira',2007,97),
(3,'978-83-246-0549-1','SQL Server 2005. Wyci�nij wszystko','Eric L. Brown',2007,57),
(4,'978-83-246-1258-1','PHP, MySQL i MVC. Tworzenie witryn WWW opartych na bazie danych','W�odzimierz Gajda',2010,79),
(5,'978-83-246-2060-9','Access 2007 PL. Seria praktyk','Andrew Unsworth',2009,39),
(6,'978-83-246-2188-0','Czysty kod. Podr�cznik dobrego programisty','Robert C. Martin',2010,67);
SET IDENTITY_INSERT Ksiazka OFF
GO

SET IDENTITY_INSERT Egzemplarz ON
INSERT INTO Egzemplarz (Egzemplarz_ID,Ksiazka_ID,Sygnatura) VALUES
(1,5,'S0001'),
(2,5,'S0002'),
(3,1,'S0003'),
(4,1,'S0004'),
(5,1,'S0005'),
-- (6,2,'S0006'),
(7,3,'S0007'),
(8,3,'S0008'),
(9,3,'S0009'),
(10,3,'S0010'),
(11,6,'S0011'),
(12,6,'S0012'),
(13,4,'S0013'),
(14,4,'S0014'),
(15,4,'S0015');
SET IDENTITY_INSERT Egzemplarz OFF
GO

SET IDENTITY_INSERT Czytelnik ON
INSERT INTO Czytelnik (CZYTELNIK_ID,PESEL,NAZWISKO,MIASTO,DATA_URODZENIA) VALUES
(1,'55101011111','Kowalski','Wroc�aw','1955-10-10'),
(2,'60101033333','Maliniak','Wroc�aw','1960-10-10'),
(3,'65120122222','Nowak','Warszawa','1965-12-01');
SET IDENTITY_INSERT Czytelnik OFF
GO

SET IDENTITY_INSERT Wypozyczenie ON
INSERT INTO Wypozyczenie (Wypozyczenie_ID,Czytelnik_ID,Egzemplarz_ID,Data,Liczba_Dni) VALUES
(1,1,3,'2020-02-01',12),
(2,1,4,'2020-01-05',20),
(3,1,15,'2020-01-21',45),
(4,2,8,'2020-01-13',7),
(5,3,4,'2020-02-01',14),
(6,3,12,'2020-02-02',10),
(7,3,12,'2020-02-12',3),
(8,3,12,'2020-02-16',4),
(9,1,12,'2020-02-20',2),
(10,2,12,'2020-02-22',5),
(11,2,12,'2020-02-28',12),
(12,1,12,'2020-03-10',8),
(13,3,12,'2020-03-15',4);
SET IDENTITY_INSERT Wypozyczenie OFF
GO



-- Zadanie 1

CREATE FUNCTION dbo.ReadersHoldingSpecimensForDays
(
    @Days INT
)
RETURNS TABLE
AS
RETURN
(
    SELECT
        c.PESEL,
        COUNT(w.Egzemplarz_ID) AS Specimens
    FROM
        Czytelnik c
    JOIN
        Wypozyczenie w ON c.Czytelnik_ID = w.Czytelnik_ID
    WHERE
        DATEDIFF(DAY, w.Data, GETDATE()) >= @Days
    GROUP BY
        c.PESEL
    HAVING
        COUNT(CASE WHEN DATEDIFF(DAY, w.Data, GETDATE()) >= @Days THEN 1 END) > 0
);

SELECT *
FROM dbo.ReadersHoldingSpecimensForDays(30);

-- Zadanie 2

CREATE TABLE firstnames
(
    id INT IDENTITY PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL
);

CREATE TABLE lastnames
(
    id INT IDENTITY PRIMARY KEY,
    lastname VARCHAR(50) NOT NULL
);

CREATE TABLE fldata
(
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    PRIMARY KEY (firstname, lastname)  
);

INSERT INTO firstnames (firstname)
VALUES ('John'), ('Jane'), ('Michael'), ('Sarah'), ('Robert');

INSERT INTO lastnames (lastname)
VALUES ('Smith'), ('Johnson'), ('Williams'), ('Brown'), ('Jones');

CREATE PROCEDURE dbo.GenerateRandomFLData
    @n INT  
AS
BEGIN
    DECLARE @totalPairs INT, @count INT;
    
    SELECT @totalPairs = (SELECT COUNT(*) FROM firstnames) * (SELECT COUNT(*) FROM lastnames);
    
    IF @n > @totalPairs
    BEGIN
        THROW 50001, 'Error: Number of requested pairs exceeds the total number of possible unique pairs.', 1;
        RETURN;
    END

    DELETE FROM fldata;

    SET @count = 0;

    WHILE @count < @n
    BEGIN
        DECLARE @firstname VARCHAR(50), @lastname VARCHAR(50);

        SELECT TOP 1 @firstname = firstname -- recursion error wtf
        FROM firstnames
        ORDER BY NEWID();

        SELECT TOP 1 @lastname = lastname
        FROM lastnames
        ORDER BY NEWID();

        -- SELECT @firstname = firstname
        -- FROM firstnames
        -- ORDER BY NEWID();

        -- SELECT @lastname = lastname
        -- FROM lastnames
        -- ORDER BY NEWID();

        IF NOT EXISTS (SELECT 1 FROM fldata WHERE firstname = @firstname AND lastname = @lastname)
        BEGIN
            INSERT INTO fldata (firstname, lastname)
            VALUES (@firstname, @lastname);

            SET @count = @count + 1;
        END
    END
END;

EXEC dbo.GenerateRandomFLData @n = 3;

-- Zadanie 3

CREATE PROCEDURE dbo.InsertNewReader
(
    @PESEL CHAR(11),
    @Nazwisko VARCHAR(30),
    @Miasto VARCHAR(30),
    @Data_Urodzenia DATE
)
AS
BEGIN
    IF LEN(@PESEL) <> 11 OR @PESEL NOT LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
    BEGIN
        THROW 50001, 'Invalid PESEL format. PESEL must consist of exactly 11 digits.', 1;
        RETURN;
    END

    IF LEN(@Nazwisko) < 2 OR @Nazwisko COLLATE Latin1_General_BIN NOT LIKE '[A-Z]%'
    BEGIN
        THROW 50002, 'Invalid last name format. Last name must start with a capital letter and be at least 2 characters long.', 1;
        RETURN;
    END

    IF @Data_Urodzenia IS NULL OR @Data_Urodzenia > GETDATE()
    BEGIN
        THROW 50003, 'Invalid birth date. Birth date must be a valid date and cannot be in the future.', 1;
        RETURN;
    END

    INSERT INTO Czytelnik (PESEL, Nazwisko, Miasto, Data_Urodzenia, Ostatnie_Wypozyczenie)
    VALUES (@PESEL, @Nazwisko, @Miasto, @Data_Urodzenia, NULL);
END;

EXEC dbo.InsertNewReader
    @PESEL = '12345678901',
    @Nazwisko = 'Kowalski',
    @Miasto = 'Warsaw',
    @Data_Urodzenia = '1990-05-15';

-- Zadanie 4

CREATE TYPE ReaderIDTableType AS TABLE
(
    Czytelnik_ID INT
);

CREATE PROCEDURE dbo.GetTotalBorrowingDays
(
    @ReaderIDs ReaderIDTableType READONLY
)
AS
BEGIN
    SELECT
        w.Czytelnik_ID,
        SUM(w.Liczba_Dni) AS Total_Borrowing_Days
    FROM
        Wypozyczenie w
    JOIN
        @ReaderIDs r ON w.Czytelnik_ID = r.Czytelnik_ID
    GROUP BY
        w.Czytelnik_ID;
END;

DECLARE @Readers ReaderIDTableType;

INSERT INTO @Readers (Czytelnik_ID)
VALUES (1), (2), (3);

EXEC dbo.GetTotalBorrowingDays @ReaderIDs = @Readers;


-- Zadanie 6
--1
DECLARE @TableVariable TABLE (ID INT, Name NVARCHAR(50))
INSERT INTO @TableVariable (ID, Name) VALUES (1, 'Table Variable')

SELECT * FROM @TableVariable

CREATE TABLE #LocalTempTable (ID INT, Name NVARCHAR(50))
INSERT INTO #LocalTempTable (ID, Name) VALUES (1, 'Local Temp Table')

SELECT * FROM #LocalTempTable

CREATE TABLE ##GlobalTempTable (ID INT, Name NVARCHAR(50))
INSERT INTO ##GlobalTempTable (ID, Name) VALUES (1, 'Global Temp Table')

SELECT * FROM ##GlobalTempTable

SELECT * FROM tempdb.INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '#%'



--2

-- SELECT * FROM #LocalTempTable

SELECT * FROM ##GlobalTempTable

SELECT * FROM tempdb.INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '##%'


-- Zadanie 5

CREATE TYPE dbo.ProductIdentifierList AS TABLE
(
    ProductID INT
);

CREATE PROCEDURE dbo.UpdateDiscontinuedDate
(
    @ProductIdentifiers dbo.ProductIdentifierList READONLY,
    @DiscontinuedDate DATE
)
AS
BEGIN
    UPDATE SalesLT.Product
    SET DiscontinuedDate = @DiscontinuedDate
    WHERE ProductID IN (SELECT ProductID FROM @ProductIdentifiers)
      AND DiscontinuedDate IS NULL;

    DECLARE @ProductID INT;
    
    DECLARE ProductCursor CURSOR FOR
    SELECT ProductID
    FROM SalesLT.Product
    WHERE ProductID IN (SELECT ProductID FROM @ProductIdentifiers)
      AND DiscontinuedDate IS NOT NULL;

    OPEN ProductCursor;
    
    FETCH NEXT FROM ProductCursor INTO @ProductID;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        PRINT 'Product with ID ' + CAST(@ProductID AS VARCHAR(10)) + ' already has a discontinued date.';
        FETCH NEXT FROM ProductCursor INTO @ProductID;
    END;

    CLOSE ProductCursor;
    DEALLOCATE ProductCursor;
END;




DECLARE @ProductList dbo.ProductIdentifierList;

INSERT INTO @ProductList (ProductID)
VALUES (1), (2), (3);

EXEC dbo.UpdateDiscontinuedDate @ProductList, '2024-01-01';