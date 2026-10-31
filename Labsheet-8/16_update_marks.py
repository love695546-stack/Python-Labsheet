# Program 16: Update the marks of a student using their ID
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    sid = int(input("Enter student ID: "))
    marks = float(input("Enter new marks: "))
    cur.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, sid))
    conn.commit()
    print("Marks updated." if cur.rowcount else "No student with that ID.")
except ValueError:
    print("Error: please enter valid numbers.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
