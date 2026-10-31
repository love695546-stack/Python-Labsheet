# Program 7: Check if a specific table exists in the database
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    name = input("Enter table name to check: ").strip()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (name,))                        # parameterized query
    if cur.fetchone():
        print(f"Table '{name}' exists.")
    else:
        print(f"Table '{name}' does NOT exist.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
