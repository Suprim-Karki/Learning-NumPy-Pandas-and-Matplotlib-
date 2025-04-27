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
# print(np.nan)   #nan = not a number and inf=infinity
# print(np.inf)

# print(np.isnan(np.sqrt(-1)))
# print(np.isinf(np.array([10])/0))


'''Mathematical operations'''

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,0]

# a1=np.array(l1)
# a2=np.array(l2)

# print(l1*5)   #prints the list 5 times
# print(a1*5)   #prints the list with its items multiplied by 5
# print(a1+5)   #this is not possible in normal list
# print(a1-5)   

# print(l1+l2)  #concats the 2 lists
# print(a1+a2)  #adds the list items like a vector

# m1=np.array([1,2,3])
# m2=np.array([[1],[2]])
# print(m1+m2)            #adds 1 to each item in m1 and again adds 2 so retruns a 2*3 array
# print(np.sqrt(m1))      #square roots each item
# print(np.sin(m1))
# print(np.cos(m1))
# print(np.log10(m1))

''' Array Methods'''
# a=np.array([1,2,3])
# a=np.append(a,[7,8,9])
# a=np.insert(a,3,[4,5,6])   #insert into array, position-1, what to insert
# print(a)

# b=np.array([[1,2,3],
#             [4,5,6]])
# b=np.delete(a,1)     #deletse element at index 1 which is 2
# b=np.delete(a,4)     #deletes element at index 1 which is 5

# c=np.delete(b,0,0)    #deletes entire 0th row, keep last parameter 0 to delete row
# c=np.delete(b,1,0)    #deletes entire 1st row which is 1,2,3
# c=np.delete(b,1,1)    #deletes entire 1st column which is 2 and 5

''' Aggregate Functions '''
a=np.array([[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [18,19,20,21,22,23]])

print(a.min())
print(a.max())
print(a.mean())
print(a.std())
print(a.sum())
print(np.median(a))