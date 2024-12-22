-- Zadanie 1

CREATE PROCEDURE dbo.backup_ProductDescription_standartquery AS
BEGIN
    CREATE TABLE ProductDescription_Backup (
        ProductDescriptionID int NOT NULL,
        Description nvarchar(400) NOT NULL,
        rowguid uniqueidentifier NOT NULL,
        ModifiedDate datetime NOT NULL
    );

    DECLARE @StartTime datetime = GETDATE();

    INSERT INTO ProductDescription_Backup
    SELECT *
    FROM SalesLT.ProductDescription;

    DECLARE @EndTime datetime = GETDATE();
    SELECT DATEDIFF(ms, @StartTime, @EndTime) AS 'ExecutionTimeInMilliseconds_standartquery';
END
GO

CREATE PROCEDURE dbo.backup_ProductDescription_cursor AS
BEGIN
    CREATE TABLE ProductDescription_Backup (
        ProductDescriptionID int NOT NULL,
        Description nvarchar(400) NOT NULL,
        rowguid uniqueidentifier NOT NULL,
        ModifiedDate datetime NOT NULL
    );

    DECLARE @StartTime datetime = GETDATE();

    DECLARE @ProductDescriptionID int;
    DECLARE @Description nvarchar(400);
    DECLARE @rowguid uniqueidentifier;
    DECLARE @ModifiedDate datetime;

    DECLARE i CURSOR FOR
    SELECT *
    FROM SalesLT.ProductDescription;

    OPEN i;
    FETCH NEXT FROM i INTO @ProductDescriptionID, @Description, @rowguid, @ModifiedDate;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        INSERT INTO ProductDescription_Backup (ProductDescriptionID, Description, rowguid, ModifiedDate)
        VALUES (@ProductDescriptionID, @Description, @rowguid, @ModifiedDate);

      FETCH NEXT FROM i INTO @ProductDescriptionID, @Description, @rowguid, @ModifiedDate;
    END;

    CLOSE i;
    DEALLOCATE i;

    DECLARE @EndTime datetime = GETDATE();
    SELECT DATEDIFF(ms, @StartTime, @EndTime) AS 'ExecutionTimeInMilliseconds_cursor';
END
GO



EXEC backup_ProductDescription_standartquery;
DROP TABLE ProductDescription_Backup;
GO

EXEC backup_ProductDescription_cursor;
DROP TABLE ProductDescription_Backup;
GO

-- Zadanie 2

-- Static Cursor: A static cursor returns a result set that is fixed at the time the cursor is opened.
-- Changes made to the data in the database after the cursor is opened are not visible through the cursor.

-- Dynamic Cursor: A dynamic cursor reflects all changes made to the rows in its result set as you scroll around the cursor. 
-- The data values, order, and membership of the rows can change on each fetch.

-- Keyset Cursor: A keyset cursor is a hybrid of static and dynamic cursors. 
-- It behaves like a dynamic cursor in that it detects changes to the membership and order of its result set when scrolling through the cursor. 
-- However, it behaves like a static cursor in that it does not detect changes to the values in the rows of its result set.
-- Changes to data values (made either by the keyset owner or other processes) are visible as the user scrolls through the result set. Inserts made outside the cursor (by other processes) are visible only if the cursor is closed and reopened. Inserts made from inside the cursor are visible at the end of the result set.

SET NOCOUNT ON;

DROP TABLE IF EXISTS numbers;
GO
CREATE TABLE numbers ( id INT PRIMARY KEY, number INT );
GO

DECLARE @a INT;
SET @a = 1;
WHILE ( @a <= 60 )
BEGIN
    INSERT INTO numbers VALUES ( @a, @a );
    SET @a = @a + 1;
END;
GO

DECLARE @limit INT;
SET @limit = 10;

-- Execute each version 3 times, analyzing results and messages
DECLARE c CURSOR FOR SELECT number FROM numbers WHERE number <= @limit;
-- DECLARE c CURSOR STATIC FOR SELECT number FROM numbers WHERE number <= @limit;
-- DECLARE c CURSOR KEYSET FOR SELECT number FROM numbers WHERE number <= @limit;

SET @limit = 20;

OPEN c;

DECLARE @currentNumber INT, @counter INT;
SET @counter = 2;

PRINT 'Next numbers from cursor:';
FETCH NEXT FROM c INTO @currentNumber;
WHILE ( @@FETCH_STATUS = 0 )
BEGIN
    PRINT @currentNumber;
    -- PRINT 'Number: ' + CAST(@currentNumber AS VARCHAR);
    -- PRINT 'Counter: ' + CAST(@counter AS VARCHAR);
    DELETE FROM numbers WHERE number = @counter;
    FETCH NEXT FROM c INTO @currentNumber;
    SET @counter = @counter + 2;
END;

PRINT 'Status of last fetch: ' + CAST(@@FETCH_STATUS AS VARCHAR);
CLOSE c;
DEALLOCATE c;

SELECT * FROM numbers WHERE number <= 10;


-- Zadanie 3

DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Rates;
DROP TABLE IF EXISTS Prices;
GO

CREATE TABLE Products(
    ID INT PRIMARY KEY,
    ProductName VARCHAR(50),
);

CREATE TABLE Rates(
    Currency VARCHAR(3) PRIMARY KEY,
    PricePLN DECIMAL(10, 2),
);

CREATE TABLE Prices(
    ProductID INT,
    Currency VARCHAR(3),
    Price DECIMAL(10, 2),

    FOREIGN KEY (ProductID) REFERENCES Products(ID),
);
GO

INSERT INTO Products (ID, ProductName) VALUES
    (1, 'Product A'),
    (2, 'Product B'),
    (3, 'Product C');

INSERT INTO Rates (Currency, PricePLN) VALUES
    ('USD', 3.75),
    ('EUR', 4.25),
    ('GBP', 4.90);

INSERT INTO Prices (ProductID, Currency, Price) VALUES
    (1, 'USD', 20.00),
    (1, 'EUR', 18.00),
    (1, 'PLN', 50.00),
    (2, 'USD', 15.50),
    (2, 'GBP', 12.75),
    (2, 'PLN', 60.00),
    (3, 'EUR', 30.00),
    (3, 'JPY', 5000.00),
    (3, 'PLN', 100.00);
GO

---------------------------------------------------------------------
DROP PROCEDURE IF EXISTS UpdatePrices
GO  

CREATE PROCEDURE UpdatePrices
AS
BEGIN 
    DECLARE PriceCursor CURSOR FOR
        SELECT ProductID, Currency, Price FROM Prices
        WHERE Currency NOT LIKE 'PLN'

    DECLARE @ProductID INT
    DECLARE @Currency VARCHAR(3)
    DECLARE @Price DECIMAL(10, 2)

    OPEN PriceCursor
    FETCH NEXT FROM PriceCursor INTO @ProductID, @Currency, @Price

    WHILE @@FETCH_STATUS = 0
    BEGIN
        DECLARE @RatePLN DECIMAL(10, 2) = NULL
        SELECT @RatePLN = PricePLN FROM Rates 
        WHERE Currency = @Currency

        IF @RatePLN IS NULL
        BEGIN
            DELETE FROM Prices
            WHERE ProductID = @ProductID AND Currency = @Currency
        END
        ELSE
        BEGIN
            DECLARE @PricePLN DECIMAL(10, 2)
            SELECT @PricePLN = Price FROM Prices 
            WHERE ProductID = @ProductID AND Currency = 'PLN'

            UPDATE Prices SET Price = @PricePLN / @RatePLN
            WHERE ProductID = @ProductID AND Currency = @Currency
        END

        FETCH NEXT FROM PriceCursor INTO @ProductID, @Currency, @Price
    END

    CLOSE PriceCursor
    DEALLOCATE PriceCursor
END
GO

---------------------------------------------------------------------
SELECT * FROM Prices
EXEC UpdatePrices
SELECT * FROM Prices

---------------------------------------------------------------------
-- DROP TABLE IF EXISTS Products;
-- DROP TABLE IF EXISTS Rates;
-- DROP TABLE IF EXISTS Prices;
-- DROP PROCEDURE IF EXISTS UpdatePrices
-- GO

-- Zadanie 4

CREATE TRIGGER trg_UpdateModifiedDate
ON SalesLT.Customer
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE SalesLT.Customer
    SET ModifiedDate = GETDATE()
    FROM SalesLT.Customer AS c
    INNER JOIN inserted AS i ON c.CustomerID = i.CustomerID;
END;
GO

--showcase
SELECT CustomerID, FirstName, LastName, ModifiedDate
FROM SalesLT.Customer
WHERE CustomerID = 1; 

UPDATE SalesLT.Customer
SET FirstName = 'UpdatedName'
WHERE CustomerID = 1;

SELECT CustomerID, FirstName, LastName, ModifiedDate
FROM SalesLT.Customer
WHERE CustomerID = 1;



-- Zadanie 5
CREATE TABLE SalesLT.ProductPriceHistory (
    ProductPriceHistoryID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT NOT NULL,
    StandardCost DECIMAL(19,4) NOT NULL,
    ListPrice DECIMAL(19,4) NOT NULL,
    EffectiveStartDate DATETIME NOT NULL DEFAULT GETDATE(),
    EffectiveEndDate DATETIME NULL,
    FOREIGN KEY (ProductID) REFERENCES SalesLT.Product(ProductID)
);

CREATE TRIGGER trg_ProductPriceHistory
ON SalesLT.Product
AFTER UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (SELECT * FROM inserted)
    BEGIN
        INSERT INTO SalesLT.ProductPriceHistory (ProductID, StandardCost, ListPrice, EffectiveStartDate)
        SELECT 
            i.ProductID,
            i.StandardCost,
            i.ListPrice,
            GETDATE()
        FROM 
            inserted i
        INNER JOIN 
            deleted d ON i.ProductID = d.ProductID
        WHERE 
            (i.StandardCost <> d.StandardCost OR i.ListPrice <> d.ListPrice);

        UPDATE SalesLT.ProductPriceHistory
        SET EffectiveEndDate = GETDATE()
        FROM SalesLT.ProductPriceHistory h
        INNER JOIN deleted d ON h.ProductID = d.ProductID
        WHERE 
            h.EffectiveEndDate IS NULL
            AND (h.StandardCost <> d.StandardCost OR h.ListPrice <> d.ListPrice);
    END

    IF EXISTS (SELECT * FROM deleted)
    BEGIN
        UPDATE SalesLT.ProductPriceHistory
        SET EffectiveEndDate = GETDATE()
        FROM SalesLT.ProductPriceHistory h
        INNER JOIN deleted d ON h.ProductID = d.ProductID
        WHERE h.EffectiveEndDate IS NULL;
    END
END;

SELECT 
    p.ProductID,
    p.Name,
    h.StandardCost,
    h.ListPrice,
    h.EffectiveStartDate,
    COALESCE(h.EffectiveEndDate, GETDATE()) AS EffectiveEndDate
FROM 
    SalesLT.Product p
INNER JOIN 
    SalesLT.ProductPriceHistory h ON p.ProductID = h.ProductID
ORDER BY 
    p.ProductID, h.EffectiveStartDate;

-- Zadanie 6
DROP TABLE IF EXISTS brands
DROP TABLE IF EXISTS brand_approvals
DROP VIEW IF EXISTS vw_brands
DROP TRIGGER IF EXISTS trg_vw_brands
GO

CREATE TABLE brands (
  brand_name VARCHAR(255)
)

CREATE TABLE brand_approvals(
    brand_id INT IDENTITY PRIMARY KEY,
    brand_name VARCHAR(255) NOT NULL
);
GO

CREATE VIEW vw_brands 
AS
SELECT
    brand_name,
    'Approved' approval_status
FROM
    brands
UNION
SELECT
    brand_name,
    'Pending Approval' approval_status
FROM
    brand_approvals;
GO

CREATE TRIGGER trg_vw_brands 
ON vw_brands
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO brand_approvals ( 
        brand_name
    )
    SELECT
        i.brand_name
    FROM
        inserted i
    WHERE
        i.brand_name NOT IN (
            SELECT 
                brand_name
            FROM
                brands
        );
END
GO

INSERT INTO vw_brands(brand_name)
VALUES('Eddy Merckx');

INSERT INTO brands(brand_name)
VALUES('Nike')

SELECT
	brand_name,
	approval_status
FROM
	vw_brands;

SELECT 
	*
FROM 
	brand_approvals;



-- Zadanie 7
CREATE TABLE book (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);

CREATE TABLE specimen (
    specimen_id INT PRIMARY KEY,
    book_id INT,
    description VARCHAR(100),
    FOREIGN KEY (book_id) REFERENCES book(book_id) ON DELETE CASCADE
);


CREATE TRIGGER trg_limit_specimens
BEFORE INSERT ON specimen
FOR EACH ROW
BEGIN
    DECLARE specimen_count INT;

    SELECT COUNT(*) INTO specimen_count
    FROM specimen
    WHERE book_id = NEW.book_id;

    IF specimen_count >= 5 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'no more than 5 specimens ok?';
    END IF;
END;

INSERT INTO book (book_id, title) VALUES (1, 'Book Title');

INSERT INTO specimen (specimen_id, book_id, description) VALUES (1, 1, 'Specimen 1');
INSERT INTO specimen (specimen_id, book_id, description) VALUES (2, 1, 'Specimen 2');
INSERT INTO specimen (specimen_id, book_id, description) VALUES (3, 1, 'Specimen 3');
INSERT INTO specimen (specimen_id, book_id, description) VALUES (4, 1, 'Specimen 4');
INSERT INTO specimen (specimen_id, book_id, description) VALUES (5, 1, 'Specimen 5');

INSERT INTO specimen (specimen_id, book_id, description) VALUES (6, 1, 'Specimen 6');


-- Zadanie 8
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT
);

CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT,
    stock_level INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);





CREATE TRIGGER trg_update_inventory
AFTER INSERT, UPDATE ON products
FOR EACH ROW
BEGIN
    DECLARE existing_stock INT;

    SELECT stock_level INTO existing_stock
    FROM inventory
    WHERE product_id = NEW.product_id;

    IF existing_stock IS NOT NULL THEN
        UPDATE inventory
        SET stock_level = stock_level + NEW.quantity
        WHERE product_id = NEW.product_id;
    ELSE
        INSERT INTO inventory (inventory_id, product_id, stock_level)
        VALUES ((SELECT ISNULL(MAX(inventory_id), 0) + 1 FROM inventory), NEW.product_id, NEW.quantity);
    END IF;
END;



CREATE TRIGGER trg_inventory_update
AFTER UPDATE ON inventory
FOR EACH ROW
BEGIN
    UPDATE products
    SET quantity = quantity + NEW.stock_level - OLD.stock_level
    WHERE product_id = NEW.product_id;
END;




INSERT INTO products (product_id, product_name, quantity) VALUES (1, 'Product A', 10);

SELECT * FROM inventory;

UPDATE products SET quantity = 5 WHERE product_id = 1;

SELECT * FROM inventory;