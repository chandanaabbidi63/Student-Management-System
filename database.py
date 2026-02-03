from db_config import get_connection

def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (student.name, student.email, student.course))
    conn.commit()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    conn.close()
    return records

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
