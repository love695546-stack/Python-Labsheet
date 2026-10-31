# Program 11: Connect to a database and create the table 'students'
import sqlite3
try:
    conn = sqlite3.connect("students_crud.db")      # creates the file if missing
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                       id    INTEGER PRIMARY KEY,   -- roll number
                       name  TEXT NOT NULL,
                       age   INTEGER,
                       marks REAL)""")
    conn.commit()
    print("Connected to database and table 'students' is ready.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Connected to database and table 'students' is ready.
