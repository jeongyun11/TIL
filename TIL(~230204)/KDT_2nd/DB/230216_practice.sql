-- 문제 1
SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (SELECT AVG(MSRP) FROM products)
ORDER BY MSRP;

-- 문제 2
SELECT customerNumber, customerName
FROM customers
WHERE customerNumber IN (
	SELECT customerNumber 
    FROM orders 
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
    )
ORDER BY customerNumber;

SELECT customerNumber, customerName
FROM customers
INNER JOIN orders USING (customerNumber)
WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
ORDER BY customerNumber;

-- 문제 3
SELECT productCode, productName, productLine, MSRP
FROM products
WHERE 
	MSRP = (SELECT max(MSRP) FROM products WHERE productLine = 'Classic Cars' );

-- 문제 4
SELECT customerNumber , customerName , country
FROM customers
WHERE country = (SELECT MAX(country) FROM customers)
ORDER BY customerNumber;

-- 문제 5
SELECT customerNumber, customerName, count(*) AS 'order_count'
FROM customers
INNER JOIN orders USING (customerNumber)
GROUP BY customerNumber
ORDER BY count(*) DESC LIMIT 1;

-- 문제 6
SELECT DISTINCT productCode, productName
FROM (SELECT * FROM orderdetails INNER JOIN products USING (productCode)) as test
WHERE 
	EXISTS (
	SELECT orderNumber 
    FROM orders 
    WHERE orderDate LIKE '2004%'
    )
ORDER BY productCode DESC;

SELECT customerNumber , customerName , country 
FROM customers 
WHERE country = (SELECT MAX(country) FROM customers);
