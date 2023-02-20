-- 1
SELECT DISTINCT lastName
FROM employees
ORDER BY lastName;

-- 2
SELECT DISTINCT lastName, firstName, officeCode
FROM employees
WHERE officeCode = 1;


-- 3
SELECT lastName, firstName, jobTitle
FROM employees
WHERE jobTitle != 'Sales Rep';

-- 4
SELECT lastName, firstName, officeCode, jobTitle
FROM employees
WHERE 
	officeCode >= 3 
	AND jobTitle = 'Sales Rep';
    
-- 5
SELECT lastName, firstName, officeCode, jobTitle
From employees
WHERE officeCode >= 3 OR jobTitle = 'Sales Rep';

-- 5
SELECT lastName, firstName, officeCode
FROM employees
-- WHERE officeCode BETWEEN 1 AND 4;
WHERE 1 <= officeCode AND officeCode <= 4 
ORDER BY officeCode;

-- 6
-- 7
SELECT lastName, firstName, officeCode
FROM employees
WHERE 
	-- officeCode = 1 OR officeCode = 3 OR officeCode = 4;
	officeCode IN (1, 3, 4);
    
--  8
SELECT lastName, firstName, officeCode
FROM employees
WHERE officeCode NOT IN (1, 3, 4);

-- 9
SELECT lastName, firstName
FROM employees
WHERE lastName LIKE '%son';

-- 10
SELECT lastName, firstName
FROM employees
WHERE firstName LIKE '___y';

-- =, >, <, != 비교연산자ALTER
--  AND OR NOT 
-- 정규표현식

-- 9
SELECT lastName, firstName
FROM employees
WHERE lastName LIKE '%son';

-- 1
SELECT firstName, officeCode
From employees
ORDER BY officeCode DESC, firstName ASC
LIMIT 5 OFFSET 3;
-- LIMIT 3, 5;

-- 1
SELECT country, AVG(creditLimit) AS avgOfCreditLimit
FROM customers
GROUP BY country -- 중복제거
ORDER BY avgOfCreditLimit DESC;

-- 2
select country, AVG(creditLimit)
FROM customers
-- WHERE AVG(creditLimit) > 80000
GROUP BY country
HAVING -- 그룹에 대한 조건
	AVG(creditLimit) > 80000; -- 여러개
    
-- 3. 데이터 조작 