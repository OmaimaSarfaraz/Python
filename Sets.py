# Set
my_set = {1, 2, 3, 4}
print(my_set)   # Output: {1, 2, 3, 4}


# Creating Sets
fruits = {"apple", "banana", "cherry"}
print(fruits)

empty_set = set()  # correct way


# Common Methods
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}