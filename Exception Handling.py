# Without Exception
num = int(input("Enter a number: "))
result = 10 / num
print("Result:", result)

# Try – Except Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input, please enter a number.")



# Finally Block
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")