# Program 17: Remove blank lines from a file
try:
    with open("sample.txt", "r") as f:
        lines = f.readlines()
    # keep only lines that contain something other than whitespace
    non_blank = [line for line in lines if line.strip()]
    with open("no_blank.txt", "w") as f:
        f.writelines(non_blank)
    print(f"Removed {len(lines) - len(non_blank)} blank line(s). Saved to no_blank.txt")
except FileNotFoundError:
    print("Error: sample.txt not found.")
