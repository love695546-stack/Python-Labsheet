# Program 19: Find the student with the highest marks from the database
import sqlite3
try:
    conn = sqlite3.connect("students_crud.db")
    cur = conn.cursor()
    cur.execute("SELECT id, name, marks FROM students ORDER BY marks DESC LIMIT 1")
    row = cur.fetchone()
    if row:
        print(f"Topper: {row[1]} (Roll {row[0]}) with {row[2]} marks")
    else:
        print("No records found.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Topper: Pooja (Roll 5) with 95.0 marks
# (database seeded first with 00_seed_database.py)
