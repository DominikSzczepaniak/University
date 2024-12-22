SELECT
    soh.SalesOrderID,
    soh.SalesOrderNumber,
    soh.PurchaseOrderNumber,
    SUM(sod.OrderQty * sod.UnitPrice) AS TotalBeforeDiscount,
    SUM(sod.LineTotal) AS TotalAfterDiscount,
    SUM((sod.OrderQty * sod.UnitPrice) - sod.LineTotal) AS TotalDiscount
FROM
    Sales.SalesOrderHeader AS soh
JOIN
    Sales.SalesOrderDetail AS sod
    ON soh.SalesOrderID = sod.SalesOrderID
GROUP BY
    soh.SalesOrderID,
    soh.SalesOrderNumber,
    soh.PurchaseOrderNumber
ORDER BY
    TotalBeforeDiscount DESC;



WITH OrderTotals AS (
    SELECT
        soh.SalesOrderID,
        soh.SalesOrderNumber,
        soh.PurchaseOrderNumber,
        SUM(sod.OrderQty * sod.UnitPrice) AS TotalBeforeDiscount,
        SUM(sod.LineTotal) AS TotalAfterDiscount,
        SUM((sod.OrderQty * sod.UnitPrice) - sod.LineTotal) AS TotalDiscount
    FROM
        Sales.SalesOrderHeader AS soh
    JOIN
        Sales.SalesOrderDetail AS sod
        ON soh.SalesOrderID = sod.SalesOrderID
    GROUP BY
        soh.SalesOrderID,
        soh.SalesOrderNumber,
        soh.PurchaseOrderNumber
)
SELECT *
FROM OrderTotals
WHERE TotalDiscount > (
    SELECT AVG(TotalDiscount) * 1.5 FROM OrderTotals
)
ORDER BY TotalDiscount DESC;