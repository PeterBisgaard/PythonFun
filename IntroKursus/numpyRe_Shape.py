import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print('Reshape From 1-D to 2-D:\n',newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print('Reshape From 1-D to 3-D:\n',newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print('Reshape array into 2x4:\n', arr.reshape(2, 4))
print('.base return originaal:\n', arr.reshape(2, 4).base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print('Reshape into unknown dimension:\n', newarr)