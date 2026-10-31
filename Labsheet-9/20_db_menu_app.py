# Program 20: Menu-driven application for all CRUD operations using a database
import sqlite3
from contextlib import contextmanager

DB_NAME = "students_crud.db"

@contextmanager
def db():
    """Open a connection, commit on success, and ALWAYS close it."""
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    with db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                            age INTEGER, marks REAL)""")

def add_student():                                  # CREATE
    sid = int(input("Roll number: "))
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with db() as conn:
        conn.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                     (sid, name, age, marks))
    print("Student added successfully.")

def view_students():                                # READ
    with db() as conn:
        rows = conn.execute("SELECT * FROM students").fetchall()
    if not rows:
        print("No records found.")
        return
    print(f"{'Roll':<6}{'Name':<10}{'Age':<6}{'Marks'}")
    for r in rows:
        print(f"{r[0]:<6}{r[1]:<10}{r[2]:<6}{r[3]}")

def update_student():                               # UPDATE
    sid = int(input("Roll number to update: "))
    marks = float(input("New marks: "))
    with db() as conn:
        cur = conn.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, sid))
    print("Marks updated." if cur.rowcount else "No student with that roll number.")

def delete_student():                               # DELETE
    sid = int(input("Roll number to delete: "))
    with db() as conn:
        cur = conn.execute("DELETE FROM students WHERE id = ?", (sid,))
    print("Record deleted." if cur.rowcount else "No student with that roll number.")

def main():
    init_db()
    actions = {"1": add_student, "2": view_students,
               "3": update_student, "4": delete_student}
    while True:
        print("\n--- Student CRUD (Database) ---")
        print("1. Add  2. View  3. Update  4. Delete  5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice in actions:
            try:
                actions[choice]()
            except ValueError:
                print("Error: please enter valid numbers.")
            except sqlite3.IntegrityError:
                print("Error: this roll number already exists.")
            except sqlite3.Error as e:
                print("Database error:", e)
        else:
            print("Invalid choice.")

main()


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
#
# --- Student CRUD (Database) ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 1
# Roll number: 6
# Name: Karan
# Age: 21
# Marks: 67
# Student added successfully.
#
# --- Student CRUD (Database) ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 2
# Roll  Name      Age   Marks
# 1     Amit      20    85.0
# 2     Riya      21    92.0
# 3     Sohan     20    35.0
# 4     Neha      22    78.0
# 5     Pooja     22    95.0
# 6     Karan     21    67.0
#
# --- Student CRUD (Database) ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 3
# Roll number to update: 1
# New marks: 95
# Marks updated.
#
# --- Student CRUD (Database) ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 4
# Roll number to delete: 2
# Record deleted.
#
# --- Student CRUD (Database) ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 2
# Roll  Name      Age   Marks
# 1     Amit      20    95.0
# 3     Sohan     20    35.0
# 4     Neha      22    78.0
# 5     Pooja     22    95.0
# 6     Karan     21    67.0
#
# --- Student CRUD (Database) ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 5
# Goodbye!
