# Program 9: Copy the contents of one file into another
try:
    with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
        dest.write(src.read())              # read source, write to destination
    print("Contents copied from sample.txt to copy.txt")
except FileNotFoundError:
    print("Error: source file not found.")
