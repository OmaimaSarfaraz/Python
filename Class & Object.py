# Simple Class & Object
class Car:
    def start(self):
        print("Car has started.")

# Object creation
mycar = Car()
mycar.start()


# Class with Attributes
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

s1 = Student("Ali", 20)
s2 = Student("Rida", 10)
s1.intro()
s2.intro()