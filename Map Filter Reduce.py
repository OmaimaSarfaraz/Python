# Map
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)  # Output: [1, 4, 9, 16]


# Filter
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]


# Reduce
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24