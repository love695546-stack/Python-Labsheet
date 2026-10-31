# Program 22: Read data from a CSV file and display it
import csv
try:
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:                  # each row is a list of strings
            print(row)
except FileNotFoundError:
    print("Error: students.csv not found.")
