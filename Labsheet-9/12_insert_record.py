# Program 12: Insert a new record into the table (Create operation)
import sqlite3
try:
    sid = int(input("Roll number (id): "))
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    conn = sqlite3.connect("students_crud.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                       id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                       age INTEGER, marks REAL)""")
    # parameterized query (?) protects against SQL injection
    cur.execute("INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
                (sid, name, age, marks))
    conn.commit()
    print("Record inserted successfully.")
except ValueError:
    print("Error: id, age and marks must be numbers.")
except sqlite3.IntegrityError:
    print("Error: a student with this roll number already exists.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Roll number (id): 6
# Name: Karan
# Age: 21
# Marks: 67
# Record inserted successfully.
# (database seeded first with 00_seed_database.py)
