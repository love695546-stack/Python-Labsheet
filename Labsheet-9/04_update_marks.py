# Program 4: Update a student's marks in the list (Update operation)
students = [
    {"roll": 1, "name": "Amit", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Sohan", "marks": 35},
]
try:
    roll = int(input("Enter roll number: "))
    new_marks = float(input("Enter new marks: "))
    for s in students:
        if s["roll"] == roll:
            s["marks"] = new_marks                  # modify the record in place
            print(f"Marks updated for {s['name']}.")
            break
    else:                                           # runs only if loop did not break
        print("Roll number not found.")
    print("Current list:", students)
except ValueError:
    print("Error: please enter valid numbers.")


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Enter roll number: 3
# Enter new marks: 90
# Marks updated for Sohan.
# Current list: [{'roll': 1, 'name': 'Amit', 'marks': 85}, {'roll': 2, 'name': 'Riya', 'marks': 92}, {'roll': 3, 'name': 'Sohan', 'marks': 90.0}]
