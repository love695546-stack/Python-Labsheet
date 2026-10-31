# Program 29: Search a record in a CSV file based on student name
import csv
try:
    name = input("Enter student name: ").strip().lower()
    found = False
    with open("students.csv", "r") as f:
        for row in csv.DictReader(f):
            if row["Name"].lower() == name:     # case-insensitive match
                print("Record found:", dict(row))
                found = True
                break
    if not found:
        print("No record found for", name)
except FileNotFoundError:
    print("Error: students.csv not found.")
