CREATE DATABASE company_db;
USE company_db;

CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Insert Departments
INSERT INTO Department VALUES (1, 'HR');
INSERT INTO Department VALUES (2, 'IT');
INSERT INTO Department VALUES (3, 'Finance');

-- Insert Employees
INSERT INTO Employee VALUES (101, 'Ravi', 2);
INSERT INTO Employee VALUES (102, 'Anita', 1);
INSERT INTO Employee VALUES (103, 'Kiran', 3);



SELECT * FROM Department;
SELECT * FROM Employee;