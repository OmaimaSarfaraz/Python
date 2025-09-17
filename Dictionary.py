# Dictionary
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
print(student)


# Accessing Values
print(student["name"])    # Output: Ali
print(student.get("age")) # Output: 20


# Updating Dictionary
student["age"] = 21
student["city"] = "Karachi"
print(student)


# Dictionary Methods
print(student.keys())   # dict_keys(['name', 'age', 'grade', 'city'])
print(student.values()) # dict_values(['Ali', 21, 'A', 'Karachi'])
print(student.items())  # key-values