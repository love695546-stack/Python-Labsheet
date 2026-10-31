# Program 25: Display students grouped by age with count in each group
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("SELECT age, COUNT(*) FROM students GROUP BY age ORDER BY age")
    print(f"{'Age':<6}{'Count'}")
    for age, count in cur.fetchall():
        print(f"{age:<6}{count}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
