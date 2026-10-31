# Program 6: CRUD operations on a dictionary of employee data
# Key = employee id, Value = dictionary of details.
employees = {}

# CREATE - add new employees
employees[101] = {"name": "Rohit", "dept": "IT", "salary": 50000}
employees[102] = {"name": "Anita", "dept": "HR", "salary": 45000}
employees[103] = {"name": "Vikas", "dept": "Sales", "salary": 40000}
print("After CREATE:", employees)

# READ - display all and one employee
print("\nREAD all employees:")
for emp_id, details in employees.items():
    print(emp_id, "->", details)
print("READ employee 102:", employees.get(102, "Not found"))

# UPDATE - change salary of employee 101
employees[101]["salary"] = 55000
print("\nAfter UPDATE (101 salary = 55000):", employees[101])

# DELETE - remove employee 103
removed = employees.pop(103, None)
print("\nAfter DELETE (103):", "removed " + removed["name"] if removed else "not found")
print("Remaining employees:", employees)


# =======================================================
# SAMPLE INPUT / OUTPUT (user input shown after each prompt)
# =======================================================
# After CREATE: {101: {'name': 'Rohit', 'dept': 'IT', 'salary': 50000}, 102: {'name': 'Anita', 'dept': 'HR', 'salary': 45000}, 103: {'name': 'Vikas', 'dept': 'Sales', 'salary': 40000}}
#
# READ all employees:
# 101 -> {'name': 'Rohit', 'dept': 'IT', 'salary': 50000}
# 102 -> {'name': 'Anita', 'dept': 'HR', 'salary': 45000}
# 103 -> {'name': 'Vikas', 'dept': 'Sales', 'salary': 40000}
# READ employee 102: {'name': 'Anita', 'dept': 'HR', 'salary': 45000}
#
# After UPDATE (101 salary = 55000): {'name': 'Rohit', 'dept': 'IT', 'salary': 55000}
#
# After DELETE (103): removed Vikas
# Remaining employees: {101: {'name': 'Rohit', 'dept': 'IT', 'salary': 55000}, 102: {'name': 'Anita', 'dept': 'HR', 'salary': 45000}}
