# To install write on terminal: pip install numpy

import numpy as np

arr = np.array([1, 2, 3, 4])

print("NumPy Array:", arr)
print("Type:", type(arr))


# Python List vs NumPy Array Speed
import numpy as np
import time

# Python list
lst = list(range(1,1000000))
start = time.time()
[x*2 for x in lst]
print("Python time:", time.time() - start)

# NumPy array
arr = np.arange(1,1000000)
start = time.time()
arr*2
print("NumPy time:", time.time() - start)