# Squares of Numbers
numbers = [x**2 for x in range(1, 6)]
print(numbers)


# Even Numbers Only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Convert Strings to Uppercase
words = ["python", "java", "c++"]
upper_words = [w.upper() for w in words]
print(upper_words)

# Nested List Comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)