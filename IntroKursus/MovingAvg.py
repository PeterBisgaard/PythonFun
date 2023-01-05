import numpy as np

# this is one dimensional array 
a = np.arange(50) 
print('Dimention: ', a.ndim)
print(a)

startPos = 0
endPos = 8
previousTwo = np.zeros(2)

actualBuffer = a.copy()

print(previousTwo)


# b is having three dimensions

# y = np.array([0.8, 0.9, 0.7, 0.6, 0.3, 0.4])

# a1 = np.array([[0,0,0,0,0], [0,0,0,0,0]])
# print(a1)
# weight = np.array([1, 2, 3, 2, 1])
# print(a1+weight)
# empty = np.zeros_like(y.size+weight.size/2)


# print(empty)
# y3 = y[0:y.size:1]
# print(y3)

