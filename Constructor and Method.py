# Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 20)
print(s1.name, s1.age)


# Method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

s1 = Student("Ali", 20)
s1.intro()


# Multiple Methods
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

c1 = Calculator(10, 5)
print("Addition:", c1.add())
print("Multiplication:", c1.multiply())