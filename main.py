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
# a=np.array([[1,2,3,4,5,6],
#             [7,8,9,10,11,12],
#             [13,14,15,16,17,18],
#             [18,19,20,21,22,23]])

# print(a.min())
# print(a.max())
# print(a.mean())
# print(a.std())
# print(a.sum())
# print(np.median(a))

''' Numpy randoms '''
# number=np.random.randint(100)
# number=np.random.randint(100, size=(2,3,4))       #min=0, max=100
# number=np.random.randint(90,100, size=(2,3,4))    #min=90,max=100

# numbers=np.random.binomial(10,p=0.5,size=(5,6))     #tries=10, probability=0.5, size of matrix(array)=5,6
# num=np.random.normal(loc=170,scale=15,size=(5,10))   #mean=170, std deviation=15
# nums=np.random.choice([10,20,30,40,50], size=(2,3))   #chooses a random number
# print(numbers)

''' Structuring methods '''

# a=np.array([[1,2,3,4,5],
#             [6,7,8,9,10],
#             [11,12,13,14,15],
#             [16,17,18,19,20]])

# print(a.shape)
# print(a.reshape((5,4)))
# print(a.reshape((20,)))     #reshapes into 1D 20 elements
# print(a.reshape((20,1)))     #reshapes into 20 rows and 1 column
# print(a.reshape((2,2,5)))    #2 collection of 2 list each of 5 collection each
# print(a.resize((2,2,5))) 

# #in reshape you need to return it to a value, i.e. a=a.reshape((5,4))
# #in resize you do not need to return it to a value, i.e. a.resize((5,4))

# print(a.flatten())    #flattens out the copy of array and doesn't affect the actual array when a variable is changed
# print(a.ravel())      #flattens out the array same as flattens but if element is changed, it also changes in the actual array

# #can also use
# var=[i for i in a.flat]
# print(var)

# print(a.transpose())  # transposes the matrix
# print(a.T)            # same as above but shorter

# #if the array is more than 2 Dimensions use swapaxes
# print(a.swapaxes(0,1))  #x and y axis
  

''' Concatenate, stacking, splitting'''

a1=np.array([[1,2,3,4,5],
     [6,7,8,9,10]])

a2=np.array([[11,12,13,14,15],
             [15,17,18,19,20]])

# a=np.concatenate((a1,a2),axis=0)     #adds the rows
# print(a)

# a=np.concatenate((a1,a2),axis=1)     #adds the elements in the columns

a=np.stack((a1,a2))     #adds the elements in a new dimension
a=np.vstack((a1,a2))    #same as concatenate at axis 0
a=np.hstack((a1,a2))     ##same as concatenate at axis 1



























