# Program 15: Replace a word in a file with another word
try:
    old = input("Word to replace: ")
    new = input("Replace with   : ")
    with open("sample.txt", "r") as f:
        content = f.read()
    updated = content.replace(old, new)     # replace all occurrences
    with open("replaced.txt", "w") as f:    # save result in a new file
        f.write(updated)
    print("Done. Output saved in replaced.txt\n")
    print(updated)
except FileNotFoundError:
    print("Error: sample.txt not found.")
