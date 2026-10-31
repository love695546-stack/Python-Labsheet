# Program 16: Display the first and last lines of a file
try:
    with open("sample.txt", "r") as f:
        lines = f.read().splitlines()
    if lines:
        print("First line:", lines[0])
        print("Last line :", lines[-1])      # index -1 is the last item
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("Error: sample.txt not found.")
