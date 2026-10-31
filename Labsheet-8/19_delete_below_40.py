# Program 19: Delete all students with marks below 40
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE marks < ?", (40,))
    conn.commit()
    print(cur.rowcount, "record(s) deleted.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
