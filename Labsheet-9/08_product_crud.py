# Program 8: Store and manage product details using CRUD operations
# Products are stored in a dictionary: product id -> details.
products = {}

while True:
    print("\n--- Product Manager ---")
    print("1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Enter choice: ").strip()
    try:
        if choice == "1":                           # CREATE
            pid = input("Product id: ").strip()
            if pid in products:
                print("Product id already exists.")
                continue
            name = input("Name: ").strip()
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            products[pid] = {"name": name, "price": price, "qty": qty}
            print("Product added.")
        elif choice == "2":                         # READ
            if not products:
                print("No products available.")
            for pid, p in products.items():
                print(f"{pid}: {p['name']} | Rs.{p['price']} | Qty {p['qty']}")
        elif choice == "3":                         # UPDATE
            pid = input("Product id to update: ").strip()
            if pid in products:
                products[pid]["price"] = float(input("New price: "))
                products[pid]["qty"] = int(input("New quantity: "))
                print("Product updated.")
            else:
                print("Product id not found.")
        elif choice == "4":                         # DELETE
            pid = input("Product id to delete: ").strip()
            if products.pop(pid, None):
                print("Product deleted.")
            else:
                print("Product id not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Error: please enter valid numbers for price/quantity.")


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
#
# --- Product Manager ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 1
# Product id: P101
# Name: Pen
# Price: 10
# Quantity: 100
# Product added.
#
# --- Product Manager ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 1
# Product id: P102
# Name: Notebook
# Price: 50
# Quantity: 40
# Product added.
#
# --- Product Manager ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 2
# P101: Pen | Rs.10.0 | Qty 100
# P102: Notebook | Rs.50.0 | Qty 40
#
# --- Product Manager ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 3
# Product id to update: P101
# New price: 12
# New quantity: 120
# Product updated.
#
# --- Product Manager ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 4
# Product id to delete: P102
# Product deleted.
#
# --- Product Manager ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 2
# P101: Pen | Rs.12.0 | Qty 120
#
# --- Product Manager ---
# 1. Add  2. View  3. Update  4. Delete  5. Exit
# Enter choice: 5
# Goodbye!
