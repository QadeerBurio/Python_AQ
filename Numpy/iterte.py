import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for val in np.nditer(arr):
    print(val, end=" ")  # Output: 1 2 3 4 5 6
for val in np.nditer(arr, op_flags=['readwrite']):
    val[...] = val * 2  # Modify in-place

print(arr)
# iterate two commonly
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10, 20, 30], [40, 50, 60]])

for x, y in np.nditer([arr1, arr2]):
    print(f"{x} + {y} = {x + y}")


#iterate with ndenumerate
arr = np.array([[10, 20], [30, 40]])

for index, value in np.ndenumerate(arr):
    print(f"Index: {index}, Value: {value}")

# order wise

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("C-order (row-wise):")
for x in np.nditer(arr, order='C'):
    print(x, end=" ")

print("\nF-order (column-wise):")
for x in np.nditer(arr, order='F'):
    print(x, end=" ")





