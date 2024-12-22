-- ALTER TABLE Sales.Customer
-- ADD CreditCardNumber NVARCHAR(20);

UPDATE Sales.SalesOrderHeader
SET CreditCardApprovalCode = '123ABC'
WHERE SalesOrderID IN (
    SELECT TOP 3 SalesOrderID 
    FROM Sales.SalesOrderHeader 
    ORDER BY NEWID()
);

UPDATE c
SET c.CreditCardNumber = 'X'
FROM Sales.Customer AS c
JOIN Sales.SalesOrderHeader AS soh
    ON c.CustomerID = soh.CustomerID
WHERE soh.CreditCardApprovalCode IS NOT NULL;

SELECT CustomerID, CreditCardNumber
FROM Sales.Customer
WHERE CreditCardNumber = 'X';

SELECT SalesOrderID, CustomerID, CreditCardApprovalCode
FROM Sales.SalesOrderHeader
WHERE CreditCardApprovalCode IS NOT NULL;

