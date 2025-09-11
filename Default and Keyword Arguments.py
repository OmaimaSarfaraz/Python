# Default Arguments
def greet(name="Student"):
    print("Hello", name)

greet()         # Output: Hello Student
greet("Ali")    # Output: Hello Ali



# Keyword Arguments
def intro(name, age):
    print("Name:", name, "Age:", age)

intro(age=20, name="Sara")



# Combining Normal + Default + Keyword
def student_info(name, course="Python", age=18):
    print("Name:", name, "| Course:", course, "| Age:", age)

student_info("Ali")
student_info("Sara", age=20)
student_info(course="Java", name="Ahmed")