# Program 21: Create and write data into a CSV file
import csv
try:
    data = [
        ["Name", "Maths", "Science", "Marks"],      # header row
        ["Amit", 80, 75, 155],
        ["Riya", 90, 85, 175],
        ["Sohan", 70, 65, 135],
        ["Neha", 88, 92, 180],
    ]
    # newline="" prevents blank lines between rows on Windows
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)              # write all rows at once
    print("students.csv created successfully.")
except Exception as e:
    print("Error:", e)
