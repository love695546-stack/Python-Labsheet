# Program 15: Display the top 3 highest scoring students
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 3")
    for rank, (name, marks) in enumerate(cur.fetchall(), start=1):
        print(f"{rank}. {name} - {marks}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
