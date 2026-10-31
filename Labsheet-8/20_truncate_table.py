# Program 20: Truncate (empty) a table while keeping its structure
# SQLite has no TRUNCATE command, so DELETE FROM is used instead.
# This is a demo table so that your students data is not lost.
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS demo_students "
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    cur.executemany("INSERT INTO demo_students (name) VALUES (?)",
                    [("A",), ("B",), ("C",)])
    cur.execute("SELECT COUNT(*) FROM demo_students")
    print("Rows before:", cur.fetchone()[0])

    cur.execute("DELETE FROM demo_students")    # removes all rows, keeps structure
    cur.execute("DELETE FROM sqlite_sequence WHERE name = ?",
                ("demo_students",))             # reset the auto-increment counter
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM demo_students")
    print("Rows after :", cur.fetchone()[0])
    cur.execute("PRAGMA table_info(demo_students)")
    print("Structure intact, columns:", [c[1] for c in cur.fetchall()])
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
