# Step 1 - Plan the Data Storage
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Priya', 'age': 30, 'department': 'Data Engineer', 'salary': 200000},
    103: {'name': 'Rajesh', 'age': 32, 'department': 'Cloud Engineer', 'salary': 150000},
    104: {'name': 'Akshay', 'age': 33, 'department': 'Project Manager', 'salary': 150000},
    105: {'name': 'Swapnil', 'age': 33, 'department': 'Testing', 'salary': 150000},
}

# Step 3 - Add Employee Functionality
def add_employee(emp_id, name ,age, department, salary):
    if emp_id in employees:
        print("Employee already exists enter a new Employee_ID: ")
    else:
        employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
        print("Employee added successfully!!")

# Step 4 - View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
    else:
        for emp_id, details in employees.items():
            print("Employee ID:", emp_id)
            print("Name:", details['name'])
            print("Age:", details['age'])
            print("Department:", details['department'])
            print("Salary:", details['salary'])
            print("------------------------")
        

#Step 5 - Search for an Employee by ID
def search_employee(emp_id):
    
    if emp_id in employees:
        emp = employees[emp_id]
        print("Employee ID:", emp_id)
        print("Name:", emp['name'])
        print("Age:", emp['age'])
        print("Department:", emp['department'])
        print("Salary:", emp['salary'])
        print("------------------------")
    
    else:
        print("Employee not found!")

# Step 2 - Define the Menu System
while True:
    print("\n====== Employee Management System ======")
    print("1: Add Employee")
    print("2: View All Employees")
    print("3: Search for Employee")
    print("4: Exit")

    opt = input("Enter option: ")

    if opt == "1":
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        add_employee(emp_id, name, age, department, salary)

    elif opt == "2":
        view_employees()

    elif opt == "3":
        emp_id = int(input("Enter Employee ID to search: "))
        search_employee(emp_id)

    elif opt == "4":
        print("Thank you for using Employee Management System!")
        break

    else:
        print("Invalid option. Please try again.")