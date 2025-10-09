# Simple Inheritance
class Animal:
    def speak(self):
        print("Animals can make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

d = Dog()
d.speak()   # From parent class
d.bark()    # From child class


# Overriding Methods
class Animal:
    def speak(self):
        print("Animals make sounds.")

class Dog(Animal):
    def speak(self):   # Overriding parent method
        print("Dog barks.")

d = Dog()
d.speak()
a = Animal()
a.speak()  


# Using super()
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

s1 = Student("Ali", 20)
s1.intro()