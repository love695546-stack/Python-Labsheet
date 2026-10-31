# Program 13: Read numbers from a file and display their sum and average
try:
    numbers = []
    with open("numbers.txt", "r") as f:
        for line in f:
            if line.strip():                # skip blank lines
                numbers.append(float(line))
    total = sum(numbers)
    print("Sum    :", total)
    print("Average:", total / len(numbers))
except FileNotFoundError:
    print("Error: numbers.txt not found.")
except ValueError:
    print("Error: file contains a non-numeric value.")
except ZeroDivisionError:
    print("Error: file has no numbers.")
