# Program 14: Count the total number of records in the table
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    print("Total records:", cur.fetchone()[0])  # fetchone returns a single tuple
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
