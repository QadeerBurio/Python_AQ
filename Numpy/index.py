import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[0])  # 10
print(arr[-1])  # 50

# Slicing
print(arr[1:4])  # [20, 30, 40]
print(arr[:3])  # [10, 20, 30]
print(arr[::2])  # [10, 30, 50]

# 2D Array Indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])  # 6
print(matrix[:, 1])  # [2, 5, 8] (2nd column)
print(matrix[:2, :2])  # Output: [[1 2] [4 5]] (Top-left 2x2 submatrix)
print(matrix[:, 1])    # Output: [2 5 8] (all rows, column 1)


# Boolean indexing
arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25])   # Output: [30 40 50]
print(arr[arr % 20 == 0])  # Output: [20 40]

# Fancy indexing
arr = np.array([10, 20, 30, 40, 50])

indices = [0, 2, 4]
print(arr[indices])  # Output: [10 30 50]
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[[0, 2], [1, 2]])  # Output: [2 9] (Elements at (0,1) and (2,2))
# 