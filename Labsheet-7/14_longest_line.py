# Program 14: Display the longest line in a file
try:
    with open("sample.txt", "r") as f:
        lines = f.read().splitlines()
    longest = max(lines, key=len)           # key=len compares by line length
    print("Longest line:", longest)
    print("Length      :", len(longest))
except FileNotFoundError:
    print("Error: sample.txt not found.")
