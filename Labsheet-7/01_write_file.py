# Program 1: Create and write text into a file
try:
    # 'w' mode creates the file (or overwrites it if it exists)
    with open("sample.txt", "w") as f:
        f.write("Python is a powerful programming language.\n")
        f.write("File handling is an important topic.\n")
        f.write("\n")
        f.write("Python makes file handling easy.\n")
        f.write("Practice makes a programmer perfect.\n")
    print("Text written to sample.txt successfully.")
except Exception as e:
    print("Error:", e)
