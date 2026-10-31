# Program 15: Update the marks of a student using roll number (Update operation)
import sqlite3
try:
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter new marks: "))
    conn = sqlite3.connect("students_crud.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, roll))
    conn.commit()
    if cur.rowcount:                                # rowcount = rows changed
        print("Marks updated successfully.")
    else:
        print("No student found with that roll number.")
except ValueError:
    print("Error: please enter valid numbers.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Enter roll number: 3
# Enter new marks: 90
# Marks updated successfully.
# (database seeded first with 00_seed_database.py)
