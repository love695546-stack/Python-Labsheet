# Program 3: Read a file line by line
try:
    with open("sample.txt", "r") as f:
        for line in f:              # iterating over file gives one line at a time
            print(line.rstrip())    # rstrip() removes the trailing newline
except FileNotFoundError:
    print("Error: sample.txt not found.")
