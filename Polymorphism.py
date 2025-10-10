# Built-in Polymorphism
print(len("Python"))   # works on string
print(len([1,2,3,4]))  # works on list


# Polymorphism with Methods
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

for animal in (Dog(), Cat()):
    print(animal.sound())


# Method Overriding (Polymorphism in OOP)
class Shape:
    def area(self):
        print("This is a generic shape.")

class Circle(Shape):
    def area(self):
        print("Area = π * r * r")

class Rectangle(Shape):
    def area(self):
        print("Area = length * width")

shapes = [Circle(), Rectangle()]
for s in shapes:
    s.area()


# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
## print(account.__balance)  #Error