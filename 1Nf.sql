CREATE DATABASE student_db;

USE student_db;

CREATE TABLE StudentCourse_1NF (
    student_id INT,
    student_name VARCHAR(50),
    course VARCHAR(50)
);

INSERT INTO StudentCourse_1NF VALUES (1, 'meghana', 'C');
INSERT INTO StudentCourse_1NF VALUES (1, 'Meghana', 'Java');
INSERT INTO StudentCourse_1NF VALUES (1, 'meghana', 'Python');
INSERT INTO StudentCourse_1NF VALUES (2, 'pavitra', 'SQL');
INSERT INTO StudentCourse_1NF VALUES (2, 'pavitra', 'DBMS');

SELECT * FROM StudentCourse_1NF;