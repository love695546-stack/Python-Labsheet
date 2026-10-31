# Program 1: Create a list of student records (Create operation)
try:
    students = []                                   # empty list to hold records
    n = int(input("How many students? "))
    for i in range(n):
        print(f"--- Student {i + 1} ---")
        roll = int(input("Roll number: "))
        name = input("Name: ").strip()
        marks = float(input("Marks: "))
        # each student is stored as a dictionary
        students.append({"roll": roll, "name": name, "marks": marks})
    print("\nStudent list created successfully:")
    print(students)
except ValueError:
    print("Error: roll number and marks must be numbers.")


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# How many students? 2
# --- Student 1 ---
# Roll number: 1
# Name: Amit
# Marks: 85
# --- Student 2 ---
# Roll number: 2
# Name: Riya
# Marks: 92
#
# Student list created successfully:
# [{'roll': 1, 'name': 'Amit', 'marks': 85.0}, {'roll': 2, 'name': 'Riya', 'marks': 92.0}]
