# Program 27: Import data from a CSV file into a database table
import csv
import sqlite3
try:
    conn = sqlite3.connect("student_db.db")
    cur = conn.cursor()
    count = 0
    with open("students_import.csv", "r") as f:
        for row in csv.DictReader(f):
            cur.execute("INSERT OR IGNORE INTO students (id, name, age, marks) "
                        "VALUES (?, ?, ?, ?)",
                        (int(row["id"]), row["name"], int(row["age"]),
                         float(row["marks"])))
            count += cur.rowcount
    conn.commit()
    print(count, "record(s) imported from students_import.csv")
except FileNotFoundError:
    print("Error: students_import.csv not found.")
except (sqlite3.Error, ValueError, KeyError) as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()
