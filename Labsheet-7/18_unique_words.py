# Program 18: Read a file and store only unique words into another file
import string
try:
    with open("sample.txt", "r") as f:
        text = f.read().lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    unique = []
    for w in text.split():
        if w not in unique:                 # keep first occurrence only
            unique.append(w)
    with open("unique_words.txt", "w") as f:
        f.write("\n".join(unique))
    print(len(unique), "unique words saved to unique_words.txt")
except FileNotFoundError:
    print("Error: sample.txt not found.")
