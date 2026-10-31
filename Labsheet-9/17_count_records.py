# Program 17: Count and display the total number of records in the table
import sqlite3
try:
    conn = sqlite3.connect("students_crud.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    print("Total number of records:", cur.fetchone()[0])
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Total number of records: 5
# (database seeded first with 00_seed_database.py)
