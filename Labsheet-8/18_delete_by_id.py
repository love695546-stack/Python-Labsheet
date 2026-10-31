# Program 18: Delete a student record using ID
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    sid = int(input("Enter student ID to delete: "))
    cur.execute("DELETE FROM students WHERE id = ?", (sid,))
    conn.commit()
    print("Record deleted." if cur.rowcount else "No student with that ID.")
except ValueError:
    print("Error: ID must be a number.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
