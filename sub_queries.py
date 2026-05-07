import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=5000,
    user="root",
    password="Ruben@123"   # replace with your MySQL password
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS tech_company_db")
cursor.execute("USE tech_company_db")

# Create Employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees(
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    dept_id INT
)
""")

# Create Departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
)
""")

# Create Projects table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Projects(
    project_id INT PRIMARY KEY,
    emp_id INT,
    project_name VARCHAR(100)
)
""")

# -----------------------------
# CLEAR OLD DATA (prevents duplicate error)
# -----------------------------
cursor.execute("DELETE FROM Employees")
cursor.execute("DELETE FROM Departments")
cursor.execute("DELETE FROM Projects")

# -----------------------------
# INSERT DATA
# -----------------------------

cursor.execute("""
INSERT INTO Employees VALUES
(1,'Ravi',50000,1),
(2,'Meena',70000,2),
(3,'Arun',60000,1),
(4,'Kiran',45000,2),
(5,'Pooja',80000,3)
""")

cursor.execute("""
INSERT INTO Departments VALUES
(1,'IT'),
(2,'HR'),
(3,'Finance')
""")

cursor.execute("""
INSERT INTO Projects VALUES
(101,1,'AI System'),
(102,2,'Payroll App'),
(103,3,'Database Tool'),
(104,5,'Finance Tracker')
""")

conn.commit()

# -----------------------------
# Requirement 1: Single Row Subquery
# -----------------------------
print("\nEmployees earning more than average salary")

cursor.execute("""
SELECT name, salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary) FROM Employees
)
""")

for row in cursor.fetchall():
    print(row)

# -----------------------------
# Requirement 2: Multiple Row Subquery
# -----------------------------
print("\nEmployees in IT or Finance department")

cursor.execute("""
SELECT name
FROM Employees
WHERE dept_id IN (
    SELECT dept_id
    FROM Departments
    WHERE dept_name IN ('IT','Finance')
)
""")

for row in cursor.fetchall():
    print(row)

# -----------------------------
# Requirement 3: Correlated Subquery
# -----------------------------
print("\nEmployees earning more than their department average")

cursor.execute("""
SELECT name, salary, dept_id
FROM Employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees e2
    WHERE e1.dept_id = e2.dept_id
)
""")

for row in cursor.fetchall():
    print(row)

# -----------------------------
# Requirement 4: Nested Subquery
# -----------------------------
print("\nEmployees working on IT department projects")

cursor.execute("""
SELECT name
FROM Employees
WHERE emp_id IN (
    SELECT emp_id
    FROM Projects
    WHERE emp_id IN (
        SELECT emp_id
        FROM Employees
        WHERE dept_id = (
            SELECT dept_id
            FROM Departments
            WHERE dept_name = 'IT'
        )
    )
)
""")

for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()