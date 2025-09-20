# Built-in Modules

# Math Module
import math
print(math.sqrt(16))       # 4.0
print(math.factorial(5))   # 120
print(math.pi)             # 3.14159
print(math.pow(2, 3))      # 8.0



# Random Module
import random
print(random.randint(1, 10))      # Random integer between 1 and 10
print(random.choice([1, 2, 3]))   # Random element from list
print(random.random())            # Random float between 0 and 1



# Datetime Module
import datetime
today = datetime.date.today()
print(today)   # Current date

now = datetime.datetime.now()
print(now)     # Current date and time