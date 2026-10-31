# Helper (not a lab question): rebuild students_crud.db with 5 sample students.
import os
import sqlite3
if os.path.exists("students_crud.db"):
    os.remove("students_crud.db")
conn = sqlite3.connect("students_crud.db")
conn.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, "
             "age INTEGER, marks REAL)")
conn.executemany("INSERT INTO students VALUES (?, ?, ?, ?)",
                 [(1, "Amit", 20, 85), (2, "Riya", 21, 92), (3, "Sohan", 20, 35),
                  (4, "Neha", 22, 78), (5, "Pooja", 22, 95)])
conn.commit()
conn.close()
print("students_crud.db created with 5 sample students.")
