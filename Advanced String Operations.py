# String Slicing (with Step)
text = "PythonProgramming"
print(text[0:6:2])   # Output: Pto


# String Membership Operators
print("Python" in "PythonProgramming")   # True
print("Java" not in "PythonProgramming") # True


# String Comparison
print("apple" < "banana")   # True
print("abc" == "ABC")       # False


# String Join and Split
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)   # Output: Python is fun


text = "apple,banana,mango"
fruits = text.split(",")
print(fruits)     # Output: ['apple', 'banana', 'mango']


# String Strip, Lstrip, Rstrip
msg = "   Hello Python   "
print(msg.strip())   # "Hello Python"


# String isX Methods (Checking)
print("Hello".isalpha())   # True
print("123".isdigit())     # True
print("Hello123".isalnum()) # True
print("   ".isspace())     # True


# Reversing a String
text = "Python"
print(text[::-1])   # nohtyP