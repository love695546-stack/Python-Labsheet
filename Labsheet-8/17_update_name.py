# Program 17: Update the name of a student
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    sid = int(input("Enter student ID: "))
    name = input("Enter new name: ").strip()
    cur.execute("UPDATE students SET name = ? WHERE id = ?", (name, sid))
    conn.commit()
    print("Name updated." if cur.rowcount else "No student with that ID.")
except ValueError:
    print("Error: ID must be a number.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
