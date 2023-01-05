import numpy as np

print('----- JOIN 2 1D array -----')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print('Concatenate (join) two 1-D arrays: \n', arr)

print('----- JOIN 2D array -----')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print('Concatenate (join) two 2-D arrays along rows (axis=1): \n', arr)

print('----- Stack (join) array using Stack function-----')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2), axis=1)
print('Stack (join) two 2-D arrays along stack (axis=1): \n', arr)

print('----- Stack array along rows -----')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.hstack((arr1, arr2))
print('Stack (join) two 2-D arrays along row using hstack: \n', arr)

print('----- Stack array along columns -----')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.vstack((arr1, arr2))
print('Stack (join) two 2-D arrays along columns using vstack: \n', arr)

print('----- Stack array along height/depth -----')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.dstack((arr1, arr2))
print('Stack (join) two 2-D arrays along height/depth using dstack: \n', arr)