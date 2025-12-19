
SELECT *
FROM Production.ProductCategory

SELECT *
FROM Production.ProductSubcategory

SELECT *
FROM Production.Product

SELECT


FROM Production.ProductCategory as pc
INNER JOIN Production.ProductSubcategory as psc ON  pc.ProductCategoryID = psc.ProductCategoryID
INNER JOIN Production.Product as p on psc.ProductSubcategoryID = p.ProductSubcategoryID