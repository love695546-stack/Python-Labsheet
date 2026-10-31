# Helper: delete student_db.db and rebuild it with sample data.
# Run this any time you want to start fresh (not part of the 30 questions).
import os
import sqlite3

DB = "student_db.db"
if os.path.exists(DB):
    os.remove(DB)                                   # remove old database file
conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("""CREATE TABLE students (
                   id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                   age INTEGER, marks REAL)""")
cur.execute("""CREATE TABLE courses (
                   course_id INTEGER PRIMARY KEY, student_id INTEGER,
                   course_name TEXT NOT NULL,
                   FOREIGN KEY (student_id) REFERENCES students(id))""")
cur.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", [
    (1, "Amit", 20, 85), (2, "Riya", 21, 92), (3, "Sohan", 20, 35),
    (4, "Neha", 22, 78), (5, "Karan", 21, 67), (6, "Pooja", 22, 95),
    (7, "Rahul", 20, 38), (8, "Sima", 21, 81)])
cur.executemany("INSERT INTO courses VALUES (?, ?, ?)", [
    (1, 1, "Python"), (2, 2, "Java"), (3, 4, "DBMS"),
    (4, 6, "AI"), (5, 1, "DBMS")])
conn.commit()
conn.close()
print("student_db.db reset with sample data.")
