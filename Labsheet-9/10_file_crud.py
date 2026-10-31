# Program 10: CRUD operations on a file (add, view, modify, delete records)
# Records are stored in records.txt, one per line: roll,name,marks
FILE = "records.txt"

def load_records():
    """Read all records from the file into a list of [roll, name, marks]."""
    try:
        with open(FILE, "r") as f:
            return [line.strip().split(",") for line in f if line.strip()]
    except FileNotFoundError:
        return []                                   # file does not exist yet

def save_records(records):
    """Write the whole list back to the file."""
    with open(FILE, "w") as f:
        for r in records:
            f.write(",".join(r) + "\n")

while True:
    print("\n--- File Records ---")
    print("1. Add  2. View  3. Modify marks  4. Delete  5. Exit")
    choice = input("Enter choice: ").strip()
    try:
        records = load_records()
        if choice == "1":                           # CREATE
            roll = input("Roll: ").strip()
            if any(r[0] == roll for r in records):
                print("Roll number already exists.")
                continue
            name = input("Name: ").strip()
            marks = input("Marks: ").strip()
            float(marks)                            # validates that marks is numeric
            records.append([roll, name, marks])
            save_records(records)
            print("Record added.")
        elif choice == "2":                         # READ
            if not records:
                print("No records found.")
            for r in records:
                print(f"Roll {r[0]} | {r[1]} | Marks {r[2]}")
        elif choice == "3":                         # UPDATE
            roll = input("Roll to modify: ").strip()
            for r in records:
                if r[0] == roll:
                    r[2] = str(float(input("New marks: ")))
                    save_records(records)
                    print("Record modified.")
                    break
            else:
                print("Roll not found.")
        elif choice == "4":                         # DELETE
            roll = input("Roll to delete: ").strip()
            new_records = [r for r in records if r[0] != roll]
            if len(new_records) < len(records):
                save_records(new_records)
                print("Record deleted.")
            else:
                print("Roll not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Error: marks must be a number.")
    except OSError as e:
        print("File error:", e)


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
#
# --- File Records ---
# 1. Add  2. View  3. Modify marks  4. Delete  5. Exit
# Enter choice: 1
# Roll: 1
# Name: Amit
# Marks: 85
# Record added.
#
# --- File Records ---
# 1. Add  2. View  3. Modify marks  4. Delete  5. Exit
# Enter choice: 1
# Roll: 2
# Name: Riya
# Marks: 92
# Record added.
#
# --- File Records ---
# 1. Add  2. View  3. Modify marks  4. Delete  5. Exit
# Enter choice: 2
# Roll 1 | Amit | Marks 85
# Roll 2 | Riya | Marks 92
#
# --- File Records ---
# 1. Add  2. View  3. Modify marks  4. Delete  5. Exit
# Enter choice: 3
# Roll to modify: 1
# New marks: 90
# Record modified.
#
# --- File Records ---
# 1. Add  2. View  3. Modify marks  4. Delete  5. Exit
# Enter choice: 4
# Roll to delete: 2
# Record deleted.
#
# --- File Records ---
# 1. Add  2. View  3. Modify marks  4. Delete  5. Exit
# Enter choice: 2
# Roll 1 | Amit | Marks 90.0
#
# --- File Records ---
# 1. Add  2. View  3. Modify marks  4. Delete  5. Exit
# Enter choice: 5
# Goodbye!
