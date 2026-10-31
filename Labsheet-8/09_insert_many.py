# Program 9: Insert multiple records into the 'students' table
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                       id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                       age INTEGER, marks REAL)""")
    records = [(2, "Riya", 21, 92), (3, "Sohan", 20, 35), (4, "Neha", 22, 78),
               (5, "Karan", 21, 67), (6, "Pooja", 22, 95), (7, "Rahul", 20, 38),
               (8, "Sima", 21, 81)]
    cur.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)", records)
    conn.commit()
    print(cur.rowcount, "record(s) inserted.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
