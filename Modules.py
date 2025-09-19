# Built-in Modules
import math
print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.14159

import random
print(random.randint(1, 10))  # Random number between 1 and 10


# Importing Specific Functions
from math import sqrt, pi
print(sqrt(25))   # 5.0
print(pi)         # 3.14159


# Creating a Custom Module
#File: mymodule.py
# Main File:

import mymodule

print(mymodule.greet("Ali"))   # Hello, Ali!
print(mymodule.add(5, 3))      # 8


# Renaming a Module (alias)
import math as m
print(m.sqrt(36))   # 6.0