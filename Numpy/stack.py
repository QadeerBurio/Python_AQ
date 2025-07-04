# vertical stacking
import numpy as np

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])

result = np.vstack((arr1, arr2))

print(result)


# horizontal stacking
result = np.hstack((arr1, arr2))

print(result)

# depth stacking
result = np.dstack((arr1, arr2))

print(result)

# column stacking
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.column_stack((arr1, arr2))

print(result)


# row stacking

result = np.vstack((arr1, arr2))

print(result)

# concatenation stacking
# result = np.concatenate((arr1, arr2), axis=0)  # Vertical stacking
# print(result)
#
# result = np.concatenate((arr1, arr2), axis=1)  # Horizontal stacking
# print(result)






# main points
#✅ vstack() → Stack arrays row-wise (vertical).
# ✅ hstack() → Stack arrays column-wise (horizontal).
# ✅ dstack() → Stack arrays depth-wise (3D).
# ✅ column_stack() → Treats 1D arrays as columns.
# ✅ row_stack() → Treats 1D arrays as rows.
# ✅ concatenate() → More control over stacking along any axis.