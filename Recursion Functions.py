# Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Countdown using Recursion
def countdown(n):
    if n == 0:
        print("Time's up!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)


# Sum of Numbers
def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)

print(sum_numbers(5))  # Output: 15