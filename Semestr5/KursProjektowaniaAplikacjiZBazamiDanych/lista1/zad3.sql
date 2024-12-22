SELECT 
    a.City, 
    COUNT(DISTINCT c.CustomerID) AS NumberOfCustomers, 
    COUNT(DISTINCT sp.BusinessEntityID) AS NumberOfSalesPersons
FROM 
    AdventureWorks.Sales.Customer AS c
JOIN 
    AdventureWorks.Person.BusinessEntityAddress AS bea 
    ON c.CustomerID = bea.BusinessEntityID
JOIN 
    AdventureWorks.Person.Address AS a 
    ON bea.AddressID = a.AddressID
LEFT JOIN 
    AdventureWorks.Sales.SalesPerson AS sp 
    ON c.TerritoryID = sp.TerritoryID
GROUP BY 
    a.City
ORDER BY 
    NumberOfCustomers DESC;