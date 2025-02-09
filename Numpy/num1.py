import numpy as np
import time
import sys


i=range(1000)
print(sys.getsizeof(5)*len(i))

arr=np.array(1000)
print(arr.size*arr.itemsize)