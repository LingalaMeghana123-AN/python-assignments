import mysql.connector
from mysql.connector import Error
conn = None 

try:
    # -----------------------------
    # Connect to MySQL
    # -----------------------------
    conn = mysql.connector.connect (
        host="127.0.0.1",
        user="root",
        password="Ruben@123"   # change this
    )

    if conn.is_connected():
        print("Connected to MySQL Server")

    cursor = conn.cursor()

    # -----------------------------
    # Create Database
    # -----------------------------
    cursor.execute("CREATE DATABASE IF NOT EXISTS university_view_db")
    cursor.execute("USE university_view_db")

    # -----------------------------
    # Create Students Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        student_id INT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(50),
        marks INT,
        attendance INT
    )
    """)

    # -----------------------------
    # Clear old data
    # -----------------------------
    cursor.execute("DELETE FROM Students")

    # -----------------------------
    # Insert Student Records
    # -----------------------------
    students = [
        (1,'Ravi','CSE',85,90),
        (2,'Meena','ECE',78,88),
        (3,'Arun','CSE',92,95),
        (4,'Kiran','ME',65,80),
        (5,'Pooja','CSE',88,91),
        (6,'Rahul','ECE',70,75),
        (7,'Sneha','IT',95,96),
        (8,'Amit','IT',82,87),
        (9,'Neha','CSE',60,70),
        (10,'Vikas','ME',84,89)
    ]

    cursor.executemany("INSERT INTO Students VALUES (%s,%s,%s,%s,%s)", students)

    conn.commit()

    # -----------------------------
    # Create VIEW
    # -----------------------------
    cursor.execute("DROP VIEW IF EXISTS eligible_scholarship_students")

    cursor.execute("""
    CREATE VIEW eligible_scholarship_students AS
    SELECT *
    FROM Students
    WHERE marks > 80 AND attendance > 85
    """)

    # -----------------------------
    # Display eligible students
    # -----------------------------
    print("\nEligible Scholarship Students:\n")

    cursor.execute("SELECT * FROM eligible_scholarship_students")

    results = cursor.fetchall()

    for row in results:
        print(row)

    # -----------------------------
    # Try inserting through VIEW
    # -----------------------------
    print("\nTrying to insert student with low marks through view...\n")

    try:
        cursor.execute("""
        INSERT INTO eligible_scholarship_students
        VALUES (11,'TestStudent','CSE',70,90)
        """)
        conn.commit()
    except Error as e:
        print("Insertion failed:", e)

except Error as e:
    print("Database Error:", e)

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nMySQL connection closed")