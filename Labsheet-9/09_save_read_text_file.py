# Program 9: Save student data into a text file and read it back
try:
    n = int(input("How many students? "))
    # WRITE - one student per line in the format: roll,name,marks
    with open("students.txt", "w") as f:
        for i in range(n):
            roll = int(input(f"Student {i + 1} roll: "))
            name = input("Name: ").strip()
            marks = float(input("Marks: "))
            f.write(f"{roll},{name},{marks}\n")
    print("\nData saved to students.txt")

    # READ - open the file again and display what was saved
    print("\nReading data back from file:")
    print(f"{'Roll':<6}{'Name':<10}{'Marks'}")
    with open("students.txt", "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(f"{roll:<6}{name:<10}{marks}")
except ValueError:
    print("Error: roll and marks must be numbers.")
except OSError as e:
    print("File error:", e)


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# How many students? 2
# Student 1 roll: 1
# Name: Amit
# Marks: 85
# Student 2 roll: 2
# Name: Riya
# Marks: 92
#
# Data saved to students.txt
#
# Reading data back from file:
# Roll  Name      Marks
# 1     Amit      85.0
# 2     Riya      92.0
