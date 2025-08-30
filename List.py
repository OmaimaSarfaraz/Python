# List of fruits
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

# Accessing Elements (Indexing)
print(fruits[0]) # apple
print(fruits[2]) # mango

# Negative indexing 
print(fruits[-1]) # orange

# Slicing
fruits = ["apple", "banana", "mango", "orange", "grape"]
print(fruits[1:4]) # ['banana', 'mango', 'orange']
print(fruits[:3]) # ['apple', 'banana', 'mango']
print(fruits[2:]) # ['mango', 'orange', 'grape']

# Changing List Items
fruits = ["apple", "banana", "mango"]
fruits[1] = "kiwi" 
print(fruits) # ['apple', 'kiwi', 'mango']

# Adding Items
fruits.append("orange") 
print(fruits)
fruits.insert(1, "grape") 
print(fruits)

# Removing Items
fruits.remove("mango")
print(fruits)
fruits.pop()
print(fruits)
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)

# Length
fruits = ["apple", "banana", "mango"]
print(len(fruits)) # 3