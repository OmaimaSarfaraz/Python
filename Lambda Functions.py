# Simple Lambda
square = lambda x: x * x
print(square(5))   # Output: 25


# With Two Arguments
add = lambda a, b: a + b
print(add(3, 7))   # Output: 10


# Even/Odd Number
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(10))   # Output: Even
print(is_even(7))    # Output: Odd