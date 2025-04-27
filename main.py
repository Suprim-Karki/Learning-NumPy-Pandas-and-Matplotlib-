import numpy as np

# arr=np.array([[1,2,3],
#                [4,5,6],
#                [7,8,9]])

# print(arr[0])
# print(arr[0,1])

# print(arr.shape)     #gives 3,3 as in 3 rows 3 columns
# print(arr.ndim)      #gives dimension of the array (2 because 2 layers)
# print(arr.size)      #total number of elements
# print(arr.dtype)     #gives data types


''' Filling arrays'''

# a=np.full((2,3,4),9)      #fills a array of 2x3x4 shapearray with 9 
# print(a)         

# b=np.zeros((3,5,2))      #fills array with zeroes
# c=b=np.ones((3,5,2))      #fills array with 1
# d=np.empty((3,5,2))       #fills the space without initializing the values
# e=np.arange(0, 100, 5)   #fill the array from=0 to=100 steps=5
# f=np.linspace(0,1000,11)  #from to how many values you want, it will evenly make fractions

'''NaN and Inf'''
print(np.nan)   #nan = not a number and inf=infinity
print(np.inf)

print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.array([10])/0))

