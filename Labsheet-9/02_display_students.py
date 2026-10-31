# Program 2: Display all student records from the list (Read operation)
students = [
    {"roll": 1, "name": "Amit", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Sohan", "marks": 35},
    {"roll": 4, "name": "Neha", "marks": 78},
    {"roll": 5, "name": "Pooja", "marks": 95},
]
if not students:
    print("No records to display.")
else:
    print(f"{'Roll':<6}{'Name':<10}{'Marks'}")
    for s in students:                              # loop through every record
        print(f"{s['roll']:<6}{s['name']:<10}{s['marks']}")


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# Roll  Name      Marks
# 1     Amit      85
# 2     Riya      92
# 3     Sohan     35
# 4     Neha      78
# 5     Pooja     95
