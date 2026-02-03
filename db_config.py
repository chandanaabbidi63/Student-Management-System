import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="chandhu sindhu63",
        database="student_db"
    )
