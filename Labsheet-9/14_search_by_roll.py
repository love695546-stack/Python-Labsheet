# Program 14: Search for a specific student by roll number
import sqlite3
try:
    roll = int(input("Enter roll number to search: "))
    conn = sqlite3.connect("students_crud.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (roll,))
    row = cur.fetchone()                            # one row or None
    if row:
        print(f"Found: Roll {row[0]}, Name {row[1]}, Age {row[2]}, Marks {row[3]}")
    else:
        print("No student found with that roll number.")
except ValueError:
    print("Error: roll number must be a number.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Enter roll number to search: 3
# Found: Roll 3, Name Sohan, Age 20, Marks 35.0
# (database seeded first with 00_seed_database.py)
