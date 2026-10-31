# Program 23: Read a CSV file and calculate the average of numeric columns
import csv
try:
    with open("students.csv", "r") as f:
        rows = list(csv.DictReader(f))      # each row becomes a dictionary
    for column in rows[0].keys():
        try:
            values = [float(r[column]) for r in rows]   # fails for text columns
            print(f"Average of {column}: {sum(values) / len(values):.2f}")
        except ValueError:
            pass                            # skip non-numeric columns (e.g. Name)
except FileNotFoundError:
    print("Error: students.csv not found.")
