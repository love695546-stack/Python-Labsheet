# Program 30: Menu-driven student management application (Add, View, Update, Delete)
import sqlite3
from contextlib import contextmanager

DB_NAME = "student_db.db"

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
    """Create the students table if it does not exist."""
    with db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                            age INTEGER, marks REAL)""")

def add_student():
    name = input("Name : ").strip()
    age = int(input("Age  : "))
    marks = float(input("Marks: "))
    with db() as conn:
        cur = conn.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                           (name, age, marks))
    print("Student added with ID", cur.lastrowid)

def view_students():
    with db() as conn:
        rows = conn.execute("SELECT * FROM students").fetchall()
    if not rows:
        print("No records found.")
        return
    print(f"{'ID':<5}{'Name':<10}{'Age':<6}{'Marks'}")
    for r in rows:
        print(f"{r[0]:<5}{r[1]:<10}{r[2]:<6}{r[3]}")

def update_student():
    sid = int(input("Student ID to update: "))
    marks = float(input("New marks: "))
    with db() as conn:
        cur = conn.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, sid))
    print("Updated." if cur.rowcount else "No student with that ID.")

def delete_student():
    sid = int(input("Student ID to delete: "))
    with db() as conn:
        cur = conn.execute("DELETE FROM students WHERE id = ?", (sid,))
    print("Deleted." if cur.rowcount else "No student with that ID.")

def main():
    init_db()
    actions = {"1": add_student, "2": view_students,
               "3": update_student, "4": delete_student}
    while True:
        print("\n--- Student Management ---")
        print("1. Add   2. View   3. Update   4. Delete   5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice in actions:
            try:
                actions[choice]()
            except ValueError:
                print("Invalid input. Please enter numbers where required.")
            except sqlite3.Error as e:
                print("Database error:", e)
        else:
            print("Invalid choice.")

main()
