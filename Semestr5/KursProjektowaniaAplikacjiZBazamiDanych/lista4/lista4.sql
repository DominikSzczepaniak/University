-- Zadanie 1
	1.	Atomicity: Ensures that a transaction is treated as a single “unit of work,” so all operations either complete successfully together or fail entirely. This prevents partial changes that could lead to data inconsistencies.
	2.	Consistency: Guarantees that each transaction transitions the database from one valid state to another, following all predefined rules and constraints. It maintains data integrity.
	3.	Isolation: Ensures that concurrently executed transactions do not interfere with each other. Each transaction operates as if it’s the only one in the system, avoiding conflicts and inconsistent results.
	4.	Durability: Ensures that once a transaction is committed, the changes are permanent, even in the case of a system crash. This is often managed through logging.

Together, these principles prevent data corruption, maintain data integrity, and make transactions predictable, even in multi-user or multi-process environments.








-- Zadanie 2

USE AdventureWorksLT;
GO

CREATE PROCEDURE UpdateProductStockAndPrice
    @ProductID int,
    @NewQuantity int,
    @NewPrice money
AS
BEGIN
    BEGIN TRANSACTION;

    SAVE TRANSACTION BeforeQuantityUpdate; -- czy to jest migawka czy realny zapis do jakiegos pliku czy cos? czy jesli uzywamy rollbacku to mamy locka na całą baze danych czy pozwalamy innym wątkom wykonywac operacje ktore zawsze sa zwracane z errorem?
	-- czy uzywanie takich rzeczy nie forsuje do dokladania kolejnej abstrakcji w kodzie uzytkowinka ze wzgledu na to ze mamy teraz w bazie danych stan ktory musimy kontrolowac? jesli mamy distributed system i jedna z komend zmieni ogolny stan bazy danych to musimy sprawdzic czy inne polaczenia wykonaly to co mialy wykonac?

    BEGIN TRY
	
        UPDATE SalesLT.Product
        SET Quantity = @NewQuantity
        WHERE ProductID = @ProductID;

        UPDATE SalesLT.Product
        SET ListPrice = @NewPrice
        WHERE ProductID = @ProductID;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION BeforeQuantityUpdate;

        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        RAISERROR('Transaction rolled back to savepoint: %s', 16, 1, @ErrorMessage);

        ROLLBACK TRANSACTION;
    END CATCH;
END;
GO

EXEC UpdateProductStockAndPrice @ProductID = 101, @NewQuantity = 500, @NewPrice = 25.99;




Imagine the Inventory Department runs this procedure nightly to adjust stock and pricing data based on supplier updates. If there’s an issue with updating stock quantities (e.g., due to constraints or data mismatches), the savepoint allows the rollback of the quantity update without affecting the pricing changes. This makes error handling more granular and keeps changes reliable.


This approach keeps parts of the transaction intact while providing a way to handle partial failures gracefully.









-- Zadanie 3

1. Dirty Read

A dirty read occurs when one transaction reads data that another uncommitted transaction has modified. If the second transaction rolls back, the first transaction ends up with invalid data.


-- Transaction T1
BEGIN TRANSACTION;
SELECT AccountBalance FROM Customer WHERE CustomerID = 1;  -- Reads $1000

-- Transaction T2 (before committing)
BEGIN TRANSACTION;
UPDATE Customer SET AccountBalance = 1200 WHERE CustomerID = 1;

-- Transaction T1 (reads uncommitted value)
SELECT AccountBalance FROM Customer WHERE CustomerID = 1;  -- Reads $1200 (dirty read)

-- Transaction T2 (rolls back)
ROLLBACK;

-- Transaction T1 (now has an invalid $1200 read)

If T2 rolls back, T1 has read a balance of $1200 that never officially existed, as the value remains $1000 after T2’s rollback.

2. Non-Repeatable Read

A non-repeatable read happens when a transaction reads the same row twice and finds different values because another transaction has modified the row and committed the change in between reads.

-- Transaction T1
BEGIN TRANSACTION;
SELECT ListPrice FROM Product WHERE ProductID = 1;  -- Reads $50

-- Transaction T2 (commits a change)
BEGIN TRANSACTION;
UPDATE Product SET ListPrice = 55 WHERE ProductID = 1;
COMMIT;

-- Transaction T1 (re-reads the same row)
SELECT ListPrice FROM Product WHERE ProductID = 1;  -- Now reads $55 (non-repeatable read)

-- Transaction T1 expected consistent results but encountered a different price.

Here, T1 experiences a non-repeatable read because the product price changes from $50 to $55 within the same transaction.

3. Phantom Read

A phantom read happens when a transaction re-executes a query and finds new rows added or deleted by another committed transaction.

Example:

	•	Transaction T1: Retrieves the count of all products below a price threshold.
	•	Transaction T2: Inserts a new product that meets the threshold condition and commits.
	•	Transaction T1: Re-executes the query and finds an extra row.

-- Transaction T1
BEGIN TRANSACTION;
SELECT COUNT(*) FROM Product WHERE ListPrice < 100;  -- Counts 5 products

-- Transaction T2 (inserts a new row and commits)
BEGIN TRANSACTION;
INSERT INTO Product (ProductID, ListPrice) VALUES (6, 90);
COMMIT;

-- Transaction T1 (re-executes the same query)
SELECT COUNT(*) FROM Product WHERE ListPrice < 100;  -- Now counts 6 products (phantom read)

-- Transaction T1 expected the same count but encountered an extra row.

In this case, T1’s query returned a different result because T2 committed a new row meeting the price condition, creating a phantom row in T1’s view.










-- Zadanie 4

Here’s a high-level explanation of the locks involved in each section of your code:

1. Repeatable Read Isolation Level

	•	Transaction Isolation Level: REPEATABLE READ ensures that any rows read during the transaction cannot be modified or deleted by other transactions until this transaction completes.
	•	Locks:
	•	When SELECT * FROM liczby runs, shared locks are placed on the rows read. These locks prevent other transactions from modifying or deleting the rows but allow other reads.
	•	When the second session attempts an UPDATE liczby SET liczba=4, it tries to obtain an exclusive lock on the row(s), but it’s blocked by the shared locks held by the first transaction.
	•	Shared locks are maintained for the duration of the transaction, ensuring that no other transaction can modify the data until the transaction commits.

2. Serializable Isolation Level

	•	Transaction Isolation Level: SERIALIZABLE is the strictest level, treating a range of rows as locked and preventing both updates and new insertions that would impact the rows read.
	•	Locks:
	•	When SELECT * FROM liczby is executed, a shared lock is placed on each row, as well as a range lock on the key range being read, which prevents other transactions from inserting new rows into that range.
	•	In the second session, an INSERT liczby VALUES (151) will be blocked, as the range lock held by the first transaction prevents changes within that range of values.
	•	The range lock ensures that any phantom reads are prevented, as new rows cannot be added that would alter the results of the original SELECT.


Summary of Locks in Each Isolation Level

	•	Repeatable Read: Maintains shared locks for the transaction duration, blocking concurrent updates.
	•	Serializable: Uses shared and range locks to prevent modifications and inserts within the read range.

Using sp_lock would reveal these locks in real-time, illustrating how each isolation level applies locks differently to maintain transaction integrity.





-- Zadanie 5

A deadlock occurs in this scenario due to the following sequence of events and locking behavior:

	1.	Session 1 (S1) starts a transaction and inserts a row into liczby1. SQL Server places an exclusive lock on the liczby1 table, preventing other sessions from modifying this row.
	2.	Session 2 (S2) starts a transaction and inserts a row into liczby2, which also places an exclusive lock on liczby2, preventing other sessions from modifying it.
	3.	Session 1 (S1) then tries to update liczby2 by setting liczba=10. However, this table is currently locked by Session 2, so Session 1 is blocked and waiting for Session 2 to release the lock on liczby2.
	4.	Session 2 (S2) then tries to update liczby1 by setting liczba=10, but Session 1 holds an exclusive lock on liczby1**. As a result, **Session 2** is now blocked, waiting for **Session 1** to release the lock on liczby1**.

This leads to a classic deadlock because:

	•	Session 1 is waiting for Session 2 to release the lock on liczby2.
	•	Session 2 is waiting for Session 1 to release the lock on liczby1.

Since both sessions are waiting for each other to release their locks, they are stuck indefinitely, causing a deadlock. SQL Server will detect this deadlock and will automatically terminate one of the transactions to resolve it, rolling back one transaction to allow the other to continue.






-- Zadanie 6

Locking Hints allow SQL queries to override the default locking behavior of the current transaction isolation level. They can be used to control the type of locks that SQL Server applies to the data, which can improve performance or prevent locking conflicts. A common locking hint is NOLOCK, which lets a query read data without acquiring shared locks, allowing the read to proceed without waiting for other transactions’ locks to be released.

Locking Hint: NOLOCK

	•	Purpose: NOLOCK allows reading data without applying shared locks. This means that:
	•	The data might be dirty (uncommitted data from other transactions).
	•	The read is not blocked by other locks, and it also doesn’t block other processes.
	•	It’s generally used in read-only scenarios where absolute accuracy isn’t critical.
	•	Usage: Commonly used as SELECT ... FROM table WITH (NOLOCK).

Example Scenario

Let’s set the transaction isolation level to Serializable (the strictest level), where shared locks are held for the entire transaction to avoid dirty, non-repeatable, and phantom reads. Then, we’ll run a SELECT with and without the NOLOCK hint to illustrate the differences.

Setup

Assume we have a table Orders with a few rows of data. We’ll simulate a read operation where one transaction attempts to SELECT data while another transaction is performing an UPDATE.

-- Creating the Orders table and inserting data
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderAmount DECIMAL(10, 2)
);

INSERT INTO Orders VALUES (1, 100.00), (2, 200.00), (3, 300.00);

1: Without NOLOCK (Serializable Isolation)

	1.	Transaction 1 (T1): Starts a transaction and updates a row in Orders.
	2.	Transaction 2 (T2): Simultaneously tries to SELECT from Orders without NOLOCK.

-- Transaction 1
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
UPDATE Orders SET OrderAmount = 150.00 WHERE OrderID = 1;

-- Transaction 2
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
SELECT * FROM Orders WHERE OrderID = 1;

-- Transaction 1 completes
COMMIT;

Locks Applied (Without NOLOCK)

	•	Transaction 1 (T1): Applies an exclusive lock (X) on the row being updated (OrderID = 1).
	•	Transaction 2 (T2): When it attempts to read the same row, it needs a shared lock (S) due to the Serializable isolation level.
	•	Result: T2 is blocked by T1’s exclusive lock until T1 commits or rolls back. This ensures T2 sees only committed data, preventing dirty reads.

2: With NOLOCK Hint (Serializable Isolation)

Now let’s add the NOLOCK hint in Transaction 2 (T2) to bypass the shared lock requirement.

-- Transaction 1
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
UPDATE Orders SET OrderAmount = 150.00 WHERE OrderID = 1;

-- Transaction 2 (with NOLOCK)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
SELECT * FROM Orders WITH (NOLOCK) WHERE OrderID = 1;

-- Transaction 1 completes
COMMIT;

Locks Applied (With NOLOCK)

	•	Transaction 1 (T1): Holds an exclusive lock (X) on the row being updated (OrderID = 1).
	•	Transaction 2 (T2): Uses NOLOCK to skip acquiring a shared lock, allowing it to read the data without waiting for T1 to release its lock.
	•	Result: T2 is not blocked by T1’s lock, allowing it to read the data instantly. However, T2 may see uncommitted data from T1 (a dirty read).

Summary of Differences

Scenario	Isolation Level	Lock Applied by T1	Lock Required by T2	T2 Behavior
Without NOLOCK	Serializable	Exclusive (X)	Shared (S)	Blocked until T1 completes
With NOLOCK	Serializable	Exclusive (X)	None	Reads instantly, dirty read possible

Using NOLOCK overrides the Serializable isolation level’s strict locking rules by bypassing shared locks, enabling faster reads but at the risk of reading uncommitted or inconsistent data.








-- Zadanie 7
Locking hints in SQL Server allow developers to override the default locking behavior defined by the transaction isolation level. A common locking hint is NOLOCK, which specifies that no shared locks are issued, and dirty reads are allowed. This can reduce blocking but risks reading uncommitted data.

Here’s an example with Serializable isolation and NOLOCK:

	1.	Without NOLOCK:
	•	In Serializable isolation, SQL Server applies a range lock on the selected data. This prevents other transactions from inserting, updating, or deleting any data within the range of the selected records until the transaction completes.

BEGIN TRANSACTION
SELECT * FROM Products WHERE Category = 'Electronics';
-- Locks: Range locks on matching rows and key-range to prevent changes in the result set
COMMIT;


	2.	With NOLOCK:
	•	Applying WITH (NOLOCK) tells SQL Server to ignore the Serializable isolation and avoid placing shared locks.
	•	Other transactions can modify data in the result set while this query is executing, which may lead to dirty reads.

BEGIN TRANSACTION
SELECT * FROM Products WITH (NOLOCK) WHERE Category = 'Electronics';
-- Locks: None (data may be dirty or uncommitted)
COMMIT;



Difference:

	•	Without NOLOCK: Strict locking is enforced with range locks, ensuring data consistency but with higher blocking risk.
	•	With NOLOCK: No locks are applied, so data might be inconsistent, but there’s less chance of blocking.