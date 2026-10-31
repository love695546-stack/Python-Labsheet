# Program 29: Use functions to insert and fetch data (modular approach)
import sqlite3

DB_NAME = "student_db.db"

def get_connection():
    """Return a new database connection."""
    return sqlite3.connect(DB_NAME)

def insert_student(name, age, marks):
    """Insert one student and return the new id."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                    (name, age, marks))
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()

def fetch_students():
    """Return all students as a list of tuples."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        return cur.fetchall()
    finally:
        conn.close()

try:
    new_id = insert_student("Anil", 23, 70)
    print("Inserted student with id", new_id)
    print("\nAll students:")
    for row in fetch_students():
        print(row)
except sqlite3.Error as e:
    print("Database error:", e)
