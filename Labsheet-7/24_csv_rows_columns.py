# Program 24: Count the number of rows and columns in a CSV file
import csv
try:
    with open("students.csv", "r") as f:
        rows = list(csv.reader(f))
    print("Total rows (with header):", len(rows))
    print("Data rows               :", len(rows) - 1)
    print("Columns                 :", len(rows[0]))
except FileNotFoundError:
    print("Error: students.csv not found.")
