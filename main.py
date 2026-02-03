from student import Student
import database

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        student = Student(name, email, course)
        database.add_student(student)
        print("✅ Student added successfully")

    elif choice == "2":
        students = database.view_students()
        for s in students:
            print(s)

    elif choice == "3":
        sid = input("Enter Student ID to delete: ")
        database.delete_student(sid)
        print("🗑️ Student deleted")

    elif choice == "4":
        print("👋 Exiting program")
        break

    else:
        print("❌ Invalid choice")
