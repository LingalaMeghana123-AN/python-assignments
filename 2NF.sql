CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50)
);

CREATE TABLE Project (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(50)
);

CREATE TABLE EmployeeProject (
    employee_id INT,
    project_id INT,
    PRIMARY KEY(employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (project_id) REFERENCES Project(project_id)
);

-- Insert Employees
INSERT INTO Employee VALUES (1, 'Ravi');
INSERT INTO Employee VALUES (2, 'Anita');

-- Insert Projects
INSERT INTO Project (project_name) VALUES ('Website Development');
INSERT INTO Project (project_name) VALUES ('Mobile App');

-- Assign Employees to Projects
INSERT INTO EmployeeProject VALUES (1, 1);
INSERT INTO EmployeeProject VALUES (1, 2);
INSERT INTO EmployeeProject VALUES (2, 1);


SELECT * FROM Employee;
SELECT * FROM Project;
SELECT * FROM EmployeeProject;