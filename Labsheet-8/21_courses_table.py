# Program 21: Create a 'courses' table and insert data into it
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS courses (
                       course_id   INTEGER PRIMARY KEY,
                       student_id  INTEGER,
                       course_name TEXT NOT NULL,
                       FOREIGN KEY (student_id) REFERENCES students(id))""")
    data = [(1, 1, "Python"), (2, 2, "Java"), (3, 4, "DBMS"),
            (4, 6, "AI"), (5, 1, "DBMS")]
    cur.executemany("INSERT OR IGNORE INTO courses VALUES (?, ?, ?)", data)
    conn.commit()
    cur.execute("SELECT * FROM courses")
    for row in cur.fetchall():
        print(row)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
