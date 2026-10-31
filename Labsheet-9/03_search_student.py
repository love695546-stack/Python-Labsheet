# Program 3: Search for a student by name in the list
students = [
    {"roll": 1, "name": "Amit", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Sohan", "marks": 35},
    {"roll": 4, "name": "Neha", "marks": 78},
    {"roll": 5, "name": "Pooja", "marks": 95},
]
name = input("Enter name to search: ").strip().lower()
found = False
for s in students:
    if s["name"].lower() == name:                   # case-insensitive match
        print("Student found:", s)
        found = True
        break
if not found:
    print(f"No student named '{name}' found.")


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Enter name to search: riya
# Student found: {'roll': 2, 'name': 'Riya', 'marks': 92}
