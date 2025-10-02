# Student Marks Record

import json   # to save data in file

students = {}

# Function defining
def add_student(name, marks):
    students[name] = marks
    print(f"Record added for {name}")

def view_students():
    if students:
        for name, marks in students.items():
            print(f"{name}: {marks}")
    else:
        print("No records found!")

def save_to_file():
    with open("students.json", "w") as f:
        json.dump(students, f)
    print("Data saved to file!")

def load_from_file():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
        print("Data loaded from file!")
    except FileNotFoundError:
        print("No previous records found!")

# Main program
load_from_file()

while True:
    print("\n---Student Marks Record---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)

    elif choice == "2":
        view_students()

    elif choice == "3": 
        save_to_file()
        print("Exiting....")
        break

    else:
        print("Invalid choice! Try again.")   