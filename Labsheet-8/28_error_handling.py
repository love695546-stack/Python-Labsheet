# Program 28: Display all database errors using exception handling
import sqlite3

conn = sqlite3.connect("student_db.db")
cur = conn.cursor()

# (description, SQL, parameters) - each one is designed to fail
tests = [
    ("Table does not exist",   "SELECT * FROM no_such_table", ()),
    ("Syntax error",           "SELEC * FROM students", ()),
    ("Duplicate primary key",  "INSERT INTO students VALUES (?, ?, ?, ?)",
                               (1, "Duplicate", 20, 50)),
    ("NOT NULL violated",      "INSERT INTO students (id, name) VALUES (?, ?)",
                               (999, None)),
    ("Wrong column name",      "SELECT salary FROM students", ()),
]

for title, sql, params in tests:
    try:
        cur.execute(sql, params)
        conn.commit()
        print(f"[OK]    {title}: no error (row may not have existed)")
    except sqlite3.IntegrityError as e:         # constraint problems
        print(f"[IntegrityError]   {title}: {e}")
    except sqlite3.OperationalError as e:       # bad SQL / missing table or column
        print(f"[OperationalError] {title}: {e}")
    except sqlite3.Error as e:                  # any other database error
        print(f"[Error]            {title}: {e}")

conn.close()
