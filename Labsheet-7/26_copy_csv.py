# Program 26: Copy data from one CSV file to another
import csv
try:
    with open("students.csv", "r") as src, \
         open("students_copy.csv", "w", newline="") as dest:
        writer = csv.writer(dest)
        for row in csv.reader(src):         # read each row and write it out
            writer.writerow(row)
    print("Data copied to students_copy.csv")
except FileNotFoundError:
    print("Error: students.csv not found.")
