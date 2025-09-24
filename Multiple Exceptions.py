# Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
except Exception as e:
    print("Unexpected Error:", e)



# Using One Line for Multiple Exceptions
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print("Error:", e)



# Custom Exceptions
class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed!")
    else:
        print("Number is:", num)

try:
    check_number(-5)
except NegativeNumberError as e:
    print("Custom Exception:", e)