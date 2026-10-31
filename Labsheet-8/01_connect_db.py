# Program 1: Connect to a SQLite database and display a success message
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")     # creates the file if missing
    print("Connected to student_db.db successfully.")
    print("SQLite version:", sqlite3.sqlite_version)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()                            # always close the connection
