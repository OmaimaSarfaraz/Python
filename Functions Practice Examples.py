# Example 1: Maximum of Three Numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Maximum is:", maximum(10, 25, 15))


# Example 2: Prime Number Check    
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False


# Example 3: Factorial Function
def factorial(n):
    result = 1
    for i in range(1, n+1):    #1*2*3*4*5*....*n
        result *= i
    return result

print("Factorial is:", factorial(5))   #120


# Example 4: Calculator Functions
def add(a, b): 
    return a + b
def sub(a, b): 
    return a - b
def mul(a, b): 
    return a * b
def div(a, b): 
    return a / b

print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", mul(10, 5))
print("Division:", div(10, 5))