# Program 11: Search for a particular word in a file
try:
    word = input("Enter word to search: ").lower()
    found = False
    with open("sample.txt", "r") as f:
        for number, line in enumerate(f, start=1):
            if word in line.lower():        # case-insensitive search
                print(f"Found '{word}' in line {number}: {line.rstrip()}")
                found = True
    if not found:
        print(f"'{word}' not found in the file.")
except FileNotFoundError:
    print("Error: sample.txt not found.")
