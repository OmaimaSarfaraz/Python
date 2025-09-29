# Nested Dictionaries
students = {
    "student1": {"name": "Ali", "age": 20, "marks": 85},
    "student2": {"name": "Sara", "age": 22, "marks": 90}
}

print(students["student1"]["name"])   # Output: Ali


# Looping through Nested Dictionaries
for key, value in students.items():
    print(key, ":", value["name"], "-", value["marks"])


# Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print(squares)


# Filter with Condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)


# Using Functions with Dictionary Comprehension
def cube(n):
    return n**3

cubes = {x: cube(x) for x in range(1, 6)}
print(cubes)