# Program 16: Delete a student record using roll number (Delete operation)
import sqlite3
try:
    roll = int(input("Enter roll number to delete: "))
    conn = sqlite3.connect("students_crud.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (roll,))
    conn.commit()
    if cur.rowcount:
        print("Record deleted successfully.")
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
# Enter roll number to delete: 3
# Record deleted successfully.
# (database seeded first with 00_seed_database.py)
