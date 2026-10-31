# Program 10: Read and display all records from the table
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    print(f"{'ID':<5}{'Name':<10}{'Age':<6}{'Marks'}")
    for row in cur.fetchall():                  # fetchall returns a list of tuples
        print(f"{row[0]:<5}{row[1]:<10}{row[2]:<6}{row[3]}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
