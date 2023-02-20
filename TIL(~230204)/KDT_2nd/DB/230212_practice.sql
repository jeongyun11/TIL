-- 1
SELECT DISTINCT country
FROM customers
ORDER BY country;

-- 2
SELECT DISTINCT state
FROM customers
ORDER BY state DESC;

-- 3
SELECT customerNumber, customerName, country
FROM customers
WHERE country != 'USA'
ORDER BY customerNumber DESC;

-- 4
SELECT *
FROM offices
WHERE city = 'Paris';

-- 5
SELECT customerNumber, customerName, country, state
FROM customers
WHERE country = 'USA' AND state = 'CA'
ORDER BY customerName DESC;

-- 6
SELECT customerNumber, customerName, country, state
FROM customers
WHERE country = 'USA' AND state IN ('CA','NY')
ORDER BY customerNumber DESC;

-- 7
SELECT customerNumber, customerName, state
FROM customers
WHERE state IN ('CA', 'NY', 'CT', 'PA')
ORDER BY customerNumber DESC;

-- 8
SELECT productCode, productName, quantityInStock
FROM products
WHERE quantityInStock < 1000
ORDER BY quantityInStock;

-- 9
SELECT productCode, productName, quantityInStock
FROM products
-- WHERE quantityInStock >= 2000 AND quantityInStock <= 3000
WHERE quantityInStock BETWEEN 2000 AND 3000
ORDER BY quantityInStock DESC;
-- 10
SELECT customerNumber, customerName, phone
FROM customers
WHERE phone LIKE '%555'
ORDER BY customerName DESC;

-- 11
SELECT productCode, quantityInStock
FROM products
