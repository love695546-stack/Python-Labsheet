# Program 5: Delete a student record by roll number (Delete operation)
students = [
    {"roll": 1, "name": "Amit", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Sohan", "marks": 35},
]
try:
    roll = int(input("Enter roll number to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)                      # remove the matching record
            print(f"Record of {s['name']} deleted.")
            break
    else:
        print("Roll number not found.")
    print("Current list:", students)
except ValueError:
    print("Error: roll number must be a number.")


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Enter roll number to delete: 2
# Record of Riya deleted.
# Current list: [{'roll': 1, 'name': 'Amit', 'marks': 85}, {'roll': 3, 'name': 'Sohan', 'marks': 35}]
