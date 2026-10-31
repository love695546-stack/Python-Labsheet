# Program 7: Write multiple lines of user input into a file
try:
    print("Enter lines of text. Type END on a new line to stop.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":   # sentinel value to stop input
            break
        lines.append(line + "\n")
    with open("user_input.txt", "w") as f:
        f.writelines(lines)                 # write all lines at once
    print("Saved", len(lines), "lines to user_input.txt")
except Exception as e:
    print("Error:", e)
