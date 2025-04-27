import numpy as np

arr=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

print(arr[0])
print(arr[0,1])

print(arr.shape)     #gives 3,3 as in 3 rows 3 columns
print(arr.ndim)      #gives dimension of the array (2 because 2 layers)
print(arr.size)      #total number of elements
print(arr.dtype)     #gives data types