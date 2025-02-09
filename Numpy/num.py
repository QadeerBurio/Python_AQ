import numpy as np

# Creating a 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.shape)  # Shape of the array (rows, columns)
print(arr.ndim)   # Number of dimensions
print(arr.size)   # Total number of elements
print(arr.dtype)  # Data type of elements
# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Creating an array with zeros
zeros = np.zeros((3, 3))
print(zeros)

# Creating an array with ones
ones = np.ones((2, 4))
print(ones)

# Creating an array with a range
arr_range = np.arange(1, 12, 4)  # Start, stop, step
print(arr_range)

