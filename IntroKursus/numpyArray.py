import numpy as np

# this is one dimensional array 
arr = np.arange(24) 
print('Dimention: ', arr.ndim)
print(arr)
print("Array... \n",arr)
print("Array datatype...",arr.dtype)
print("Our Array Shape...",arr.shape)
print("Elements in the Array...",arr.size)

print('----------------------')

# now reshape it into 2 arrays with the dimension of 3 rows and 4 collums
b = arr.reshape(2,3,4) 
print(b)
print("Array... \n",b)
print("Array datatype...",b.dtype)
print("Our Array Shape...",b.shape)
print("Elements in the Array...",b.size)

print('----- Slicing 1D -----')
print('Slice elements from index 1 to index 5 from the following array: ', arr[1:5])
print('Slice elements from index 4 to the end of the array: ', arr[4:])
print('Slice elements from the beginning to index 4 (not included): ',arr[:4])
print('Slice from the index 3 from the end to index 1 from the end: ', arr[-3:-1])
print('Return every other element from index 1 to index 5: ', arr[1:5:2])
print('Return every other element from the entire array: ', arr[::2])

print('----- Slicing 2D -----')
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Array... \n',c)
print('From the second element, slice elements from index 1 to index 4 (not included): ', c[1, 1:4])
print('From both elements, return index 2: ', c[0:2, 2])
print('From both elements, slice index 1 to index 4 (not included), this will return a 2-D array: ', c[0:2, 1:4])