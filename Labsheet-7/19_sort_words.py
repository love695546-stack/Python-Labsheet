# Program 19: Sort all words in a file alphabetically and save to a new file
import string
try:
    with open("sample.txt", "r") as f:
        text = f.read().lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = sorted(text.split())            # alphabetical order
    with open("sorted_words.txt", "w") as f:
        f.write("\n".join(words))
    print("Sorted words saved to sorted_words.txt")
    print(words)
except FileNotFoundError:
    print("Error: sample.txt not found.")
