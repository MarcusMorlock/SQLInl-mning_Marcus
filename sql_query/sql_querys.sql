
SELECT *
FROM Production.ProductCategory

SELECT *
FROM Production.ProductSubcategory

SELECT *
FROM Production.Product


SELECT *
FROM Sales.SalesOrderDetail

SELECT

    pc.Name as Productname,
    COUNT(DISTINCT(p.ProductID)) as amount

FROM Production.ProductCategory as pc
INNER JOIN Production.ProductSubcategory as psc ON  pc.ProductCategoryID = psc.ProductCategoryID
INNER JOIN Production.Product as p on psc.ProductSubcategoryID = p.ProductSubcategoryID 
GROUP BY pc.Name


SELECT

    pc.Name as Productname,
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
GROUP BY YEAR(soh.OrderDate), MONTH(soh.OrderDate)
ORDER BY  YEAR(soh.OrderDate), MONTH(soh.OrderDate) ASC