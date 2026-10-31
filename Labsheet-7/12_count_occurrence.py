# Program 12: Count the occurrence of a specific word in a file
import string
try:
    word = input("Enter word to count: ").lower()
    with open("sample.txt", "r") as f:
        text = f.read().lower()
    # remove punctuation so "python." is counted as "python"
    text = text.translate(str.maketrans("", "", string.punctuation))
    count = text.split().count(word)        # count exact word matches
    print(f"'{word}' occurs {count} time(s).")
except FileNotFoundError:
    print("Error: sample.txt not found.")
