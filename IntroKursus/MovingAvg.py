import numpy as np

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w



y = np.array([0.8, 0.9, 0.7, 0.6, 0.3, 0.4])


weight = np.array([1, 2, 3, 2, 1])
empty = np.zeros_like(y.size+weight.size/2)


import numpy as np 
a = np.arange(10) 
print(a)
s = slice(0,y.size,1) 
o = a[s]
print(o)

