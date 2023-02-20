-- 1
CREATE TABLE IF NOT EXISTS users (
	userId INT AUTO_INCREMENT,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	birthday DATE NOT NULL,
	city VARCHAR(100),
	country VARCHAR(100),
	email VARCHAR(100),
	create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (userId)
);

-- 2
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01', NULL, NULL, 'beemo@hphk.kr'),
	('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', NULL),
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', NULL),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', NULL);

-- 3
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('Yunwon', 'Jeong', '1996-12-23', 'Gwangju', 'Korea', 'uwn1004@gmail.com'),
	('Diane', 'Murphy', '1985-02-14', 'Busan', 'Korea', 'dmurphy@classicmodelcars.com'),
    ('Mary', 'Patterson', '1967-09-17', 'Dokyo', 'Japan', 'mpatterso@classicmodelcars.com'),
    ('Jeff', 'Firrelli', '2002-12-08', 'Deagu', 'Korea', 'jfirrelli@classicmodelcars.com');

-- 4
UPDATE users
SET 
	first_name = 'Yunwon',
	last_name = 'Jeong',
	birthday = '1996-12-23'
WHERE
	userId = 2;

-- 5 미해결
UPDATE users
SET country = 'Korea'
WHERE country IS NULL;

-- 6
DELETE FROM users
WHERE first_name = 'Beemo';

-- 7
DELETE FROM users
WHERE 
	first_name = 'Kwangsoo'
	AND last_name = 'Lee';

-- 8
DELETE FROM users
ORDER BY userId DESC
LIMIT 1;

# set sql_safe_updates=0;
# DROP TABLE IF EXISTS users; 
# SHOW COLUMNS FROM users;
# SELECT * FROM users;