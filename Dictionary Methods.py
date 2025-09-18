# Dictionary Methods

# Keys & Values
student = {"name": "Ali", "age": 20, "grade": "A"}
print(student.keys())     
print(student.values())   
print(student.items())   


# Add & Update
student["city"] = "Karachi"   
student["age"] = 21           
print(student)


# Remove
student.pop("grade")   
print(student)

student.clear()        
print(student)


# Update Method
student = {"name": "Ali", "age": 20}
student.update({"age": 22, "grade": "A"})
print(student)


# Looping in Dictionary

# Loop through keys:
for key in student:
    print(key)


# Loop through values:
for value in student.values():
    print(value)


# Loop through items:
for key, value in student.items():
    print(key, ":", value)