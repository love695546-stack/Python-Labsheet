# Program 3: Create table 'students' with columns (id, name, age, marks)
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY,
            name  TEXT NOT NULL,
            age   INTEGER,
            marks REAL
        )""")
    conn.commit()                               # save the change
    print("Table 'students' created successfully.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
