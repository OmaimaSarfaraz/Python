# NumPy Practice + Small Exercises
import numpy as np
arr = np.array([5, 10, 15, 20, 25])

# Access first element
print(arr[0])

# Access last element
print(arr[-1])  


# Exercise 2 — Slice Array
arr = np.array([5, 10, 15, 20, 25])
print(arr[:3])


# Exercise 3 — Multi-dimensional Indexing
arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

# Second row, third column
print(arr2d[1,2])

# Third row, first column
print(arr2d[2,0])


# Exercise 4 — Vectorized Operations
arr = np.array([2, 4, 6, 8])
print(arr * 3)
print(arr - 2)


# Exercise 5 — Boolean Indexing
arr = np.array([3, 6, 5, 12, 2])
print(arr[arr <= 5])


# Exercise 6 — Combine Operations
arr = np.array([1, 2, 5, 6])
arr[arr>4]= arr[arr > 4] * 2
print(arr)