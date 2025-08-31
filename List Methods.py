# append(item)
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits) # ['apple', 'banana', 'mango']

# insert(index, item)
fruits.insert(1, "orange")
print(fruits) # ['apple', 'orange', 'banana', 'mango']

# remove(item)
fruits.remove("banana")
print(fruits) # ['apple', 'orange', 'mango']

# pop(index)
fruits.pop() # removes last element
fruits.pop(0) # removes first element

# sort()
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers) # [1, 2, 3, 4]

# reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers) # [4, 3, 2, 1]

# copy()
fruits = ["apple", "banana"]
new_fruits = fruits.copy()
print(new_fruits) # ['apple', 'banana']

# count(item)
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2)) # 3

# index(item)
fruits = ["apple", "banana", "mango"]
print(fruits.index("mango")) # 2

# Looping in List

#Directly through items
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Using index with range()
fruits = ["apple", "banana", "mango"]
for i in range(len(fruits)):
    print(fruits[i])

#Method 3: Using while loop
fruits = ["apple", "banana", "mango"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1