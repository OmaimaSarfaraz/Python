class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating Object

s1 = Student("Ali", 20)
s1.intro()