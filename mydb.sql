CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;



CREATE TABLE student (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(50)
);

INSERT INTO student (name, age, department)
VALUES 
('Pavithra', 21, 'Computer Science'),
('Navya',24,'cyber security'),
('Manasa', 22, 'Information Technology'),
('meghana', 20, 'Electronics'),
('Lavanya',23,'Computer science');

SELECT * FROM student;