# Program 5: Count the number of lines and characters in a file
try:
    with open("sample.txt", "r") as f:
        text = f.read()
    lines = text.splitlines()       # list of lines
    print("Number of lines     :", len(lines))
    print("Number of characters:", len(text))
except FileNotFoundError:
    print("Error: sample.txt not found.")
