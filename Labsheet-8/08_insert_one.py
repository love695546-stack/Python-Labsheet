# Program 8: Insert a single record into the 'students' table
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                       id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                       age INTEGER, marks REAL)""")
    # INSERT OR IGNORE skips the row if this id already exists
    cur.execute("INSERT OR IGNORE INTO students (id, name, age, marks) "
                "VALUES (?, ?, ?, ?)", (1, "Amit", 20, 85))
    conn.commit()
    print("Record inserted." if cur.rowcount else "Record with id 1 already exists.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
