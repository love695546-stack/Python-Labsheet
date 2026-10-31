# Program 5: List all tables in the connected database
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    # sqlite_master stores information about all objects in the database
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' "
                "AND name NOT LIKE 'sqlite_%'")
    tables = cur.fetchall()
    print("Tables in database:")
    for (name,) in tables:
        print(" -", name)
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
