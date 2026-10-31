# Program 25: Append a new record to an existing CSV file
import csv
try:
    new_record = ["Karan", 60, 70, 130]
    with open("students.csv", "a", newline="") as f:    # 'a' = append mode
        csv.writer(f).writerow(new_record)
    print("Record appended. Current file:")
    with open("students.csv", "r") as f:
        print(f.read())
except Exception as e:
    print("Error:", e)
