# Program 11: Display only specific columns (name and marks)
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT name, marks FROM students")
    print(f"{'Name':<10}{'Marks'}")
    for name, marks in cur.fetchall():
        print(f"{name:<10}{marks}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
