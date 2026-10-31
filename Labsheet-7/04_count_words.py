# Program 4: Count the number of words in a text file
try:
    with open("sample.txt", "r") as f:
        text = f.read()
    words = text.split()            # split() breaks text on any whitespace
    print("Number of words:", len(words))
except FileNotFoundError:
    print("Error: sample.txt not found.")
