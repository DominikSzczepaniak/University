SELECT 
    pc.Name AS CategoryName, 
    p.Name AS ProductName
FROM 
    AdventureWorks.Production.Product p
JOIN 
    AdventureWorks.Production.ProductCategory pc 
    ON p.ProductSubcategoryID = pc.ProductCategoryID
WHERE EXISTS (
    SELECT 1 
    FROM 
        AdventureWorks.Production.ProductCategory sub_pc 
    WHERE 
        sub_pc.ProductCategoryID = pc.ProductCategoryID
);