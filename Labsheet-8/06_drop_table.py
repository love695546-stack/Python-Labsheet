# Program 6: Drop (delete) a table from the database
# A demo table is created first so your real tables are not lost.
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS demo_table (id INTEGER)")
    name = input("Enter table name to drop [demo_table]: ").strip() or "demo_table"
    if not name.isidentifier():                 # table names cannot use ? so validate
        raise ValueError("Invalid table name.")
    cur.execute(f"DROP TABLE IF EXISTS {name}")
    conn.commit()
    print(f"Table '{name}' dropped (if it existed).")
except (sqlite3.Error, ValueError) as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()
