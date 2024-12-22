ALTER TABLE Sales.SalesOrderHeader
ADD CONSTRAINT CK_SalesOrderHeader_ShipDate 
CHECK (ShipDate >= OrderDate);

INSERT INTO Sales.SalesOrderHeader (OrderDate, ShipDate) 
VALUES ('2024-01-01', '2023-12-31');

ALTER TABLE SalesOrderHeader NOCHECK CONSTRAINT CK_SalesOrderHeader_ShipDate;

ALTER TABLE SalesOrderHeader CHECK CONSTRAINT CK_SalesOrderHeader_ShipDate;

SELECT * FROM Sales.SalesOrderHeader WHERE ShipDate < OrderDate;