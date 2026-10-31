# Program 30: Combine multiple CSV files into one single file
import csv
files = ["students.csv", "students2.csv", "students3.csv"]
try:
    with open("combined.csv", "w", newline="") as out:
        writer = csv.writer(out)
        header_written = False
        for name in files:
            with open(name, "r") as f:
                reader = csv.reader(f)
                header = next(reader)           # first row is the header
                if not header_written:          # write header only once
                    writer.writerow(header)
                    header_written = True
                writer.writerows(reader)        # write remaining data rows
    print("Combined", len(files), "files into combined.csv")
except FileNotFoundError as e:
    print("Error:", e)
