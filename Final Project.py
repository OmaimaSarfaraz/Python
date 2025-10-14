# All in One Python Project

def calculator():
    print("Calculator Selected")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a+b)

def todo_list():
    print("To-Do List Selected")
    tasks = []
    tasks.append(input("Enter new task: "))
    print("Tasks:", tasks)

def quiz_game():
    print("Quiz Game Selected")
    q = input("What is the capital of Pakistan? ")
    if q.lower() == "islamabad":
        print("Correct!")
    else:
        print("Wrong!")

def password_generator():
    import random, string
    print("Password Generator Selected")
    chars = string.ascii_letters + string.digits
    password = "".join(random.choice(chars) for i in range(8))
    print("Generated Password:", password)

def number_guessing():
    import random
    print("Number Guessing Game Selected")
    num = random.randint(1, 10)
    guess = int(input("Guess a number (1-10): "))
    if guess == num:
        print("Correct Guess!")
    else:
        print("Wrong! The number was", num)

while True:
    print("\n--- Mini Projects Menu ---")
    print("1. Calculator")
    print("2. To-Do List")
    print("3. Quiz Game")
    print("4. Password Generator")
    print("5. Number Guessing Game")
    print("6. Exit")
   
    choice = int(input("Enter your choice: "))

    if choice == 1:
        calculator()
    elif choice == 2:
        todo_list()
    elif choice == 3:
        quiz_game()
    elif choice == 4:
        password_generator()
    elif choice == 5:
        number_guessing()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")