#############################################################################################################
# Task: Calculate the moving average of a data array with a array of weights
#       The moving average is calculated by multiplying each data point with the corresponding weight and
#       then summing up the result. The result is then divided by the sum of the weights.
#       The solution is made in two ways
#       1) The moving average is calculated by using a "traditional" programming approach with a buffer and a tailing.
#       2) The moving average is calculated by using a convolution.
#############################################################################################################
import numpy as np

weight = np.array([1, 2, 3, 2, 1])
y = np.array([0.8, 0.9, 0.7, 0.6, 0.3, 0.4])
print(y)

############################# Solution in "traditinal" programming (wihtout convolution) ###############################
startPos = 0
endPos = y.size
tailing = np.zeros(2)
result = np.zeros(y.size)

actualBuffer = np.concatenate((tailing, y, tailing), axis=0)    # add tailing to the beginning and end of the data array due to task description
print(actualBuffer)

# Loop over the data array and calculate the moving average according to task description
for i in range(startPos, endPos):
    result[i] = (actualBuffer[i]*weight[0] + actualBuffer[i+1]*weight[1] + actualBuffer[i+2]*weight[2] + actualBuffer[i+3]*weight[3] + actualBuffer[i+4]*weight[4]) / weight.sum()

print("Traditionel: ", result)



############################# Solution with convolution ###############################
# Calculate running average of y with a array of weights
result = np.convolve(y, weight, mode='same') / weight.sum() # se description below for mode parameter
print("Convolution: ", result)

# https://stackoverflow.com/questions/20036663/understanding-numpys-convolve
# https://stackoverflow.com/questions/71309358/what-is-the-best-way-to-implement-1d-convolution-in-python
# https://en.wikipedia.org/wiki/Convolution

# From: https://numpy.org/doc/stable/reference/generated/numpy.convolve.html
    # def convolve(a, v, mode='full'):
    #     """
    #     Returns the discrete, linear convolution of two one-dimensional sequences.
    #     The convolution operator is often seen in signal processing, where it
    #     models the effect of a linear time-invariant system on a signal [1]_.  In
    #     probability theory, the sum of two independent random variables is
    #     distributed according to the convolution of their individual
    #     distributions.
    #     If `v` is longer than `a`, the arrays are swapped before computation.
    #     Parameters
    #     ----------
    #     a : (N,) array_like
    #         First one-dimensional input array.
    #     v : (M,) array_like
    #         Second one-dimensional input array.
    #     mode : {'full', 'valid', 'same'}, optional
    #         'full':
    #         By default, mode is 'full'.  This returns the convolution
    #         at each point of overlap, with an output shape of (N+M-1,). At
    #         the end-points of the convolution, the signals do not overlap
    #         completely, and boundary effects may be seen.
    #         'same':
    #         Mode 'same' returns output of length ``max(M, N)``.  Boundary
    #         effects are still visible.
    #         'valid':
    #         Mode 'valid' returns output of length
    #         ``max(M, N) - min(M, N) + 1``.  The convolution product is only given
    #         for points where the signals overlap completely.  Values outside
    #         the signal boundary have no effect.
