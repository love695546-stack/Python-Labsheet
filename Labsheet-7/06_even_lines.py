# Program 6: Display only even-numbered lines from a file
try:
    with open("sample.txt", "r") as f:
        # enumerate with start=1 so the first line is line number 1
        for number, line in enumerate(f, start=1):
            if number % 2 == 0:     # even line number
                print(number, ":", line.rstrip())
except FileNotFoundError:
    print("Error: sample.txt not found.")
