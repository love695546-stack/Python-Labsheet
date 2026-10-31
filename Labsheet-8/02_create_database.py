# Program 2: Create a new database
# In SQLite, connecting to a file that does not exist creates a new database.
import os
import sqlite3
try:
    db_name = "student_db.db"
    conn = sqlite3.connect(db_name)
    conn.commit()
    print(f"Database '{db_name}' created.")
    print("File exists on disk:", os.path.exists(db_name))
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if 'conn' in locals():
        conn.close()
