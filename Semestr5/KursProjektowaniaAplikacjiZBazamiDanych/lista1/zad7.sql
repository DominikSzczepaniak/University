CREATE TABLE Test (
    TestID INT IDENTITY(1000, 10), 
    TestName NVARCHAR(100)
);

INSERT INTO Test (TestName) VALUES ('Sample 1');
INSERT INTO Test (TestName) VALUES ('Sample 2');

SELECT @@IDENTITY AS LastIdentityValue;

SELECT IDENT_CURRENT('Test') AS LastTestIdentityValue;

-- Różnica między @@IDENTITY a IDENT_CURRENT:
-- @@IDENTITY zwraca ostatnią wartość IDENTITY w bieżącej sesji,
-- IDENT_CURRENT zwraca ostatnią wartość IDENTITY w określonej tabeli.