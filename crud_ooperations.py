import pymysql

def connect():
    return pymysql.connect(
        host="127.0.0.1",
        port=5000,  
        user="root",
        password="Ruben@123",
        database="mydb"
    )

# ✅ INSERT
def insert_student():
    connection = connect()
    cursor = connection.cursor()

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")

    sql = "INSERT INTO student (name, age, department) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, age, department))
    connection.commit()

    print("✅ Student inserted successfully!")
    connection.close()


# ✅ VIEW
def view_students():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    print("\n📌 Student Records:")
    for row in rows:
        print(row)

    connection.close()


# ✅ UPDATE
def update_student():
    connection = connect()
    cursor = connection.cursor()

    student_id = int(input("Enter Student ID to update: "))
    new_department = input("Enter New Department: ")

    sql = "UPDATE student SET department=%s WHERE id=%s"
    cursor.execute(sql, (new_department, student_id))
    connection.commit()

    print("✅ Student updated successfully!")
    connection.close()


# ✅ DELETE
def delete_student():
    connection = connect()
    cursor = connection.cursor()

    student_id = int(input("Enter Student ID to delete: "))

    sql = "DELETE FROM student WHERE id=%s"
    cursor.execute(sql, (student_id,))
    connection.commit()

    print("✅ Student deleted successfully!")
    connection.close()


# ✅ MENU SYSTEM
while True:
    print("\n===== Student Management System =====")
    print("1. Insert Student")
    print("2. View Students")
    print("3. Update Student Department")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        insert_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")