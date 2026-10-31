# Program 18: Display all records sorted by student name
import sqlite3
try:
    conn = sqlite3.connect("students_crud.db")
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, marks FROM students ORDER BY name ASC")
    print(f"{'Roll':<6}{'Name':<10}{'Age':<6}{'Marks'}")
    for r in cur.fetchall():
        print(f"{r[0]:<6}{r[1]:<10}{r[2]:<6}{r[3]}")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Roll  Name      Age   Marks
# 1     Amit      20    85.0
# 4     Neha      22    78.0
# 5     Pooja     22    95.0
# 2     Riya      21    92.0
# 3     Sohan     20    35.0
# (database seeded first with 00_seed_database.py)
