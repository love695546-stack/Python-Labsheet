# Program 13: Retrieve data sorted by marks in descending order
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY marks DESC")
    for row in cur.fetchall():
        print(row)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
