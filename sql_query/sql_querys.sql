
SELECT *
FROM Production.ProductCategory

SELECT *
FROM Production.ProductSubcategory

SELECT *
FROM Production.Product


SELECT *
FROM Sales.SalesOrderDetail

SELECT

    pc.Name as ProductName,
    COUNT(DISTINCT(p.ProductID)) as amount

FROM Production.ProductCategory as pc
INNER JOIN Production.ProductSubcategory as psc ON  pc.ProductCategoryID = psc.ProductCategoryID
INNER JOIN Production.Product as p on psc.ProductSubcategoryID = p.ProductSubcategoryID 
GROUP BY pc.Name


SELECT

    pc.Name as ProductName,
    SUM(sod.LineTotal) as Revenue

FROM Production.ProductCategory as pc
INNER JOIN Production.ProductSubcategory as psc ON  pc.ProductCategoryID = psc.ProductCategoryID
INNER JOIN Production.Product as p on psc.ProductSubcategoryID = p.ProductSubcategoryID 
INNER JOIN Sales.SalesOrderDetail as sod on p.ProductID = sod.ProductID
GROUP BY pc.Name
ORDER BY SUM(sod.LineTotal) DESC



SELECT *
FROM Sales.SalesOrderDetail

SELECT *
FROM Sales.SalesOrderHeader

SELECT

    YEAR(soh.OrderDate) as OrderYear,
    MONTH(soh.OrderDate) as OrderMonth,
    SUM(sod.LineTotal) as Revenue

FROM Sales.SalesOrderHeader as soh
INNER JOIN Sales.SalesOrderDetail as sod on soh.SalesOrderID = sod.SalesOrderID
WHERE YEAR(soh.OrderDate) < 2025
GROUP BY YEAR(soh.OrderDate), MONTH(soh.OrderDate)
ORDER BY  YEAR(soh.OrderDate), MONTH(soh.OrderDate) ASC


SELECT

    YEAR(soh.OrderDate) as OrderYear,
    MONTH(soh.OrderDate) as OrderMonth,
    SUM(soh.SubTotal) as Revenue

FROM Sales.SalesOrderHeader as soh
WHERE YEAR(soh.OrderDate) < 2025
GROUP BY YEAR(soh.OrderDate), MONTH(soh.OrderDate)
ORDER BY YEAR(soh.OrderDate), MONTH(soh.OrderDate) ASC

SELECT

COUNT(*) as AmountOrders,
YEAR(soh.OrderDate) as OrderYear,
SUM(soh.SubTotal) as Revenue

FROM Sales.SalesOrderHeader as soh
GROUP BY YEAR(soh.OrderDate)
ORDER BY YEAR(soh.OrderDate) ASC

SELECT *
FROM Production.Product


SELECT *
FROM Sales.SalesOrderDetail


SELECT TOP 10

p.Name as ProductName,
SUM(sod.LineTotal) as Revenue

FROM Production.Product as p
INNER JOIN Sales.SalesOrderDetail as sod ON p.ProductID = sod.ProductID
GROUP BY p.Name
ORDER BY Revenue DESC

SELECT 
*
FROM Sales.SalesTerritory

SELECT
*
FROM Sales.SalesOrderHeader

SELECT
*
FROM Sales.Customer


SELECT

    COUNT(DISTINCT(c.CustomerID)) as AmountCustomers,
    st.Name as Region,
    SUM(soh.SubTotal) as Revenue

FROM Sales.Customer as c
INNER JOIN Sales.SalesOrderHeader as soh on c.CustomerID = soh.CustomerID
INNER JOIN Sales.SalesTerritory as st on soh.TerritoryID = st.TerritoryID
GROUP BY st.Name
ORDER BY Revenue DESC

SELECT
*
FROM Sales.SalesTerritory

SELECT
*
FROM Sales.SalesOrderHeader

SELECT
*
FROM Sales.Customer

SELECT
*
FROM Sales.Store


SELECT

    st.Name AS Region,
    CASE
        WHEN c.StoreID IS NOT NULL THEN 'Store'
        ELSE 'Private'
    END AS CustomerType,
    SUM(soh.SubTotal) AS TotalRevenue,
    COUNT(soh.SalesOrderID) AS OrderCount,
    SUM(soh.SubTotal) * 1.0 / COUNT(soh.SalesOrderID) AS AvgOrderValue

FROM Sales.SalesOrderHeader as soh
INNER JOIN Sales.Customer as c on soh.CustomerID = c.CustomerID
INNER JOIN Sales.SalesTerritory as st on c.TerritoryID = st.TerritoryID
GROUP BY
    st.Name,
    CASE
        WHEN c.StoreID IS NOT NULL THEN 'Store'
        ELSE 'Private'
    END
ORDER BY AvgOrderValue DESC;
