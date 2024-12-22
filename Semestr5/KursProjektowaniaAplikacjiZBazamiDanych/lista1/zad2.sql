SELECT 
    pm.Name AS ProductModelName, 
    COUNT(p.ProductID) AS NumberOfProducts
FROM 
    AdventureWorks.Production.Product p
JOIN 
    AdventureWorks.Production.ProductModel pm 
    ON p.ProductModelID = pm.ProductModelID
GROUP BY 
    pm.Name
HAVING 
    COUNT(p.ProductID) > 1;

-- Jeśli używamy ProductModel.Name do grupowania, każda unikalna nazwa modelu zostanie potraktowana jako osobna grupa. Oznacza to, że różne modele produktów z tą samą nazwą (jeśli takie by istniały) byłyby liczone osobno.
