# Program 27: Display specific columns (Name and Marks) from a CSV file
import csv
try:
    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        print(f"{'Name':<10}{'Marks':>6}")
        for row in reader:
            print(f"{row['Name']:<10}{row['Marks']:>6}")
except FileNotFoundError:
    print("Error: students.csv not found.")
except KeyError as e:
    print("Error: column not found:", e)
