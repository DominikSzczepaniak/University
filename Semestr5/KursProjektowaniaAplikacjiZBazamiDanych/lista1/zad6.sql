SELECT
    p.LastName,
    p.FirstName,
    SUM(sod.OrderQty * sod.UnitPrice * sod.UnitPriceDiscount) AS TotalDiscountSaved
FROM
    Sales.Customer AS c
JOIN
    Person.Person AS p
    ON c.PersonID = p.BusinessEntityID
JOIN
    Sales.SalesOrderHeader AS soh
    ON c.CustomerID = soh.CustomerID
JOIN
    Sales.SalesOrderDetail AS sod
    ON soh.SalesOrderID = sod.SalesOrderID
GROUP BY
    p.LastName,
    p.FirstName
ORDER BY
    TotalDiscountSaved DESC;