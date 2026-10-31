# Program 24: Find the average marks of all students
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT AVG(marks) FROM students")
    avg = cur.fetchone()[0]
    print("Average marks:", round(avg, 2) if avg is not None else "No data")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
