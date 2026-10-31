# Program 4: Describe the structure of the 'students' table
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(students)")  # SQLite's version of DESCRIBE
    print(f"{'Col#':<5}{'Name':<10}{'Type':<10}{'NotNull':<9}{'Default':<9}{'PK'}")
    for cid, name, ctype, notnull, default, pk in cur.fetchall():
        print(f"{cid:<5}{name:<10}{ctype:<10}{notnull:<9}{str(default):<9}{pk}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
