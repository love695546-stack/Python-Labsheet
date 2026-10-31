# Program 12: Retrieve records where marks are greater than 80
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE marks > ?", (80,))
    for row in cur.fetchall():
        print(row)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
