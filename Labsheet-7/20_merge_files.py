# Program 20: Merge two text files into a third file
try:
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, \
         open("merged.txt", "w") as out:
        out.write(f1.read())                # first file's content
        out.write(f2.read())                # followed by second file's content
    print("file1.txt and file2.txt merged into merged.txt")
except FileNotFoundError as e:
    print("Error:", e)
