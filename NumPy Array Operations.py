# Indexing in NumPy Arrays
import numpy as np

arr = np.array([10, 20, 30, 40])  # 0,1,2,3
print(arr[0])  # Access first element
print(arr[3])  # Access fourth element


# Slicing in NumPy Arrays
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])  # Elements from index 1 to 3


# Multi-Dimensional Array Indexing
arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(arr2d[0,1])  # First row, second column
print(arr2d[2,2])  # Third row, third column


# Vectorized Operations
arr = np.array([1,2,3,4])
print(arr * 2)  # Multiply each element by 2
print(arr + 5)  # Add 5 to each element


# Boolean Indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25])  # Elements greater than 25