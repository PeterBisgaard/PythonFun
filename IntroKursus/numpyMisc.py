import numpy as np


# Count number of occurrences of a specified element in an array
arr = np.array([41, 42, 43, 41, 44])
no = np.count_nonzero(arr == 41)
print(no)


# Count number of occurrences of a specified element in an array
arr = np.array([41, 42, 43, 41, 44, 43])
no = np.count_nonzero(arr <= 42)
print(no)


#count number of occurrences of each value in array of non-negative ints
arr = np.array([0, 1, 6, 1, 4, 1, 2, 2, 2])
no = np.bincount(arr)
print(no)

# Create an empty list
filter_arr = []

# go through each element in arr
for element in no:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element == 3:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)