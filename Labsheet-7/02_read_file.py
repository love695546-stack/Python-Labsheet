# Program 2: Read the entire content of a text file
try:
    with open("sample.txt", "r") as f:
        content = f.read()          # read() returns whole file as one string
    print(content)
except FileNotFoundError:
    print("Error: sample.txt not found.")
