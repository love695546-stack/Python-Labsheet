# Program 8: Append new content to an existing file
try:
    # 'a' mode adds to the end without erasing existing content
    with open("sample.txt", "a") as f:
        f.write("This line was appended later.\n")
    print("Content appended. Updated file:\n")
    with open("sample.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error:", e)
