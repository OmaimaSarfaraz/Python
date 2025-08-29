# Numbers in python
x = 10
y = 3.14
z = 2 + 3j
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'complex'>


# Basic Math Functions
#abs(x) → Absolute value
print(abs(-5)) # 5
# pow(x, y) → Power (x^y)
print(pow(2, 3)) # 8
# round(x) → Rounds number to nearest integer
print(round(3.7)) # 4
print(round(3.14159, 2)) # 3.14
# min() & max() → Find smallest/largest value
print(min(2, 5, 7, 1)) # 1
print(max(2, 5, 7, 1)) # 7 

import math 
# math.sqrt(x) → Square root
print(math.sqrt(25)) # 5.0
# math.ceil(x) → Rounds up
print(math.ceil(4.2)) # 5
# math.floor(x) → Rounds down
print(math.floor(4.9)) # 4
# math.pi → Value of π (pi)
print(math.pi) # 3.141592653589793
# math.factorial(x) → Factorial
print(math.factorial(5)) # 120

import random
# random.random() → Random float [0.0, 1.0)
print(random.random())
# random.randint(a, b) → Random integer between a &b
print(random.randint(1, 6)) # like dice roll
# random.choice(list) → Randomly picks one element
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# Real-life Examples

print("You rolled:", random.randint(1,6))



fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Today you should eat:", random.choice(fruits))



num = int(input("Enter a number: "))
print("Square root is:", math.sqrt(num))


num = float(input("Enter a decimal number: "))
print("Rounded value is:", round(num))



colors = ["Red", "Blue", "Green", "Yellow"]
print("Your lucky color today is:", random.choice(colors))

"""Write a Python program that takes a number as input, prints its absolute value, 
its square root, and also prints a random lucky number between 1 and 10."""