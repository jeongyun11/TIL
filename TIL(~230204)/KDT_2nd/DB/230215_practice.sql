SELECT * FROM employees;
SELECT * FROM offices;

--  1
SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
ON employees.officeCode = offices.officeCode
ORDER BY employeeNumber;

-- 2 # '사무실이 없는 직원을 포함한' 모든 직원을 출력한다.
SELECT customerNumber ,officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
ON offices.city = customers.city 
ORDER BY customerNumber DESC;

-- 3 # '빈 사무실을 포함한' 모든 사무실을 출력한다.
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 4
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
INNER JOIN offices
ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 5 ∩∪
# 2. customers '사무실이 없는 직원을 포함한' 모든 직원.
# 3. offices '직원이 없는 사무실을 포함한' 모든 사무실.
# 4. (customers ∩ offices) 사무실이 있는 직원 or 직원이 있는 사무실

-- 6
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
ON customers.city = offices.city

UNION

SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
ON customers.city = offices.city

ORDER BY customerNumber DESC;

-- 7
SELECT orderdetails.orderNumber, orderDate
FROM orderdetails
INNER JOIN orders
ON orderdetails.orderNumber = orders.orderNumber;

-- 8
SELECT orderNumber, orderdetails.productCode, productName
FROM orderdetails
INNER JOIN products
ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;

-- 9
SELECT orderdetails.orderNumber, orderdetails.productCode, orderDate, productName
FROM orderdetails
INNER JOIN orders
ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;

-- 
SELECT * FROM orders;
SELECT * FROM orderdetails;
SELECT * FROM products;

