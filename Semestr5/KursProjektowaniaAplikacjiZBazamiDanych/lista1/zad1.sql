SELECT 
    DISTINCT a.City
FROM 
    Sales.SalesOrderHeader soh
JOIN 
    Person.Address a 
    ON soh.ShipToAddressID = a.AddressID
WHERE 
    soh.ShipDate IS NOT NULL
ORDER BY 
    a.City;