import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Element-wise operations
print(a + b)  # [11 22 33 44]
print(a - b)  # [9 18 27 36]
print(a * b)  # [10 40 90 160]
print(a / b)  # [10. 10. 10. 10.]

# Broadcasting
c = np.array([[1], [2], [3]])  # 3x1
d = np.array([4, 5, 6])  # 1x3
print(c + d)  # Broadcasts to 3x3






# import numpy as np

# arr =np.array([1,2,3,4,5])
# print(arr)
# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr_2d)
# arr_2d.ndim
# arr_2d.dtype
# linspace_arr = np.linspace(0, 1, 5)
# print(linspace_arr)
# arr_2d
# arr_2d.size
# arr_2d.shape
# arr_2d.reshape(3,2)
# arr_2d.ravel()
# arr_2d.min()
# arr_2d.max()
# arr_2d.sum()
# arr_2d.sum(axis=1)
# arr_2d.sum(axis=0)
# np.sqrt(arr_2d)
# np.std(arr_2d)
