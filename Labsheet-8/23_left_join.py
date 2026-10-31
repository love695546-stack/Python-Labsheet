# Program 23: LEFT JOIN between students and courses
# Shows ALL students; course is None if the student has no course.
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("""SELECT s.id, s.name, c.course_name
                   FROM students s
                   LEFT JOIN courses c ON s.id = c.student_id""")
    print(f"{'ID':<5}{'Name':<10}{'Course'}")
    for sid, name, course in cur.fetchall():
        print(f"{sid:<5}{name:<10}{course}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
