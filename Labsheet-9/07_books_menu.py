# Program 7: Menu-driven CRUD on a list of books (Add, View, Update, Delete)
books = []              # list of dictionaries
next_id = 1             # auto-increment id for each new book

while True:
    print("\n--- Book Manager ---")
    print("1. Add  2. View  3. Update price  4. Delete  5. Exit")
    choice = input("Enter choice: ").strip()
    try:
        if choice == "1":                           # CREATE
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            price = float(input("Price: "))
            books.append({"id": next_id, "title": title,
                          "author": author, "price": price})
            print(f"Book added with id {next_id}.")
            next_id += 1
        elif choice == "2":                         # READ
            if not books:
                print("No books available.")
            for b in books:
                print(f"{b['id']}. {b['title']} by {b['author']} - Rs.{b['price']}")
        elif choice == "3":                         # UPDATE
            bid = int(input("Book id to update: "))
            price = float(input("New price: "))
            for b in books:
                if b["id"] == bid:
                    b["price"] = price
                    print("Price updated.")
                    break
            else:
                print("Book id not found.")
        elif choice == "4":                         # DELETE
            bid = int(input("Book id to delete: "))
            for b in books:
                if b["id"] == bid:
                    books.remove(b)
                    print("Book deleted.")
                    break
            else:
                print("Book id not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Error: please enter a valid number.")


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
#
# --- Book Manager ---
# 1. Add  2. View  3. Update price  4. Delete  5. Exit
# Enter choice: 1
# Title: Python Basics
# Author: Guido
# Price: 450
# Book added with id 1.
#
# --- Book Manager ---
# 1. Add  2. View  3. Update price  4. Delete  5. Exit
# Enter choice: 1
# Title: DBMS
# Author: Korth
# Price: 600
# Book added with id 2.
#
# --- Book Manager ---
# 1. Add  2. View  3. Update price  4. Delete  5. Exit
# Enter choice: 2
# 1. Python Basics by Guido - Rs.450.0
# 2. DBMS by Korth - Rs.600.0
#
# --- Book Manager ---
# 1. Add  2. View  3. Update price  4. Delete  5. Exit
# Enter choice: 3
# Book id to update: 1
# New price: 500
# Price updated.
#
# --- Book Manager ---
# 1. Add  2. View  3. Update price  4. Delete  5. Exit
# Enter choice: 4
# Book id to delete: 2
# Book deleted.
#
# --- Book Manager ---
# 1. Add  2. View  3. Update price  4. Delete  5. Exit
# Enter choice: 2
# 1. Python Basics by Guido - Rs.500.0
#
# --- Book Manager ---
# 1. Add  2. View  3. Update price  4. Delete  5. Exit
# Enter choice: 5
# Goodbye!
