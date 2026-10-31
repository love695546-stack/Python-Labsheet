# Program 28: Find and display the highest marks from a CSV file
import csv
try:
    with open("students.csv", "r") as f:
        rows = list(csv.DictReader(f))
    top = max(rows, key=lambda r: float(r["Marks"]))   # compare by numeric Marks
    print("Highest marks:", top["Marks"])
    print("Scored by    :", top["Name"])
except FileNotFoundError:
    print("Error: students.csv not found.")
except (KeyError, ValueError):
    print("Error: problem reading the Marks column.")
