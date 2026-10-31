# Program 10: Read a file and convert its content to uppercase
try:
    with open("sample.txt", "r") as f:
        content = f.read().upper()          # upper() converts all letters to capitals
    print(content)
    with open("uppercase.txt", "w") as f:   # also save the result
        f.write(content)
except FileNotFoundError:
    print("Error: sample.txt not found.")
