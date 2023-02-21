SELECT * FROM employees;
SELECT * FROM offices;

--  1
SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
ON employees.officeCode = offices.officeCode
ORDER BY employeeNumber;

SELECT * FROM employees;
SELECT * FROM offices;
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


SELECT * FROM customers;
SELECT * FROM offices;
저기서 customers와 offices를 city로 연결했다는 뜻은 customers.city는 '고객사무실의 위치' 로 봤습니다
만약 customers.city가 london이여도 '정확한 사무실의 주소'가 offices.city가 london인 사무실과 다르면 잘못된 결과가 나오는 거라고 생각합니다.
-- 5 # 
# 2. customers 'offices사무실에 안 다니는 직원을 포함한' 모든 직원. 
# 3. offices 'customers고객이 안 다니는 사무실을 포함한' 모든 사무실.
# 4. (customers ∩ offices) customers고객중 offices사무실에만 다니는 고객 or offices사무실중 customers고객만 다니는 사무실

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
ORDER BY orderNumber
W
-- 
SELECT * FROM orders;
SELECT * FROM orderdetails;
SELECT * FROM products;

