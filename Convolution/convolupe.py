# From: https://www.educative.io/answers/what-is-the-numpyconvolve-method-in-python

# import numpy
import numpy as np
# create arrays using np.array
actualBuffer = np.array(range(1,15,2))
print("ActualBuffer: ", actualBuffer)

weight = np.array([1,2,1])
print("Weight: ", weight)

# compute  discrete, linear convolution 
# and store the result in result 
# By default mode='full'
result = np.convolve(actualBuffer, weight)
print("Convolve without any mode:     ",result)
# using mode='same' argument
result = np.convolve(actualBuffer, weight, mode='same')
print(f"using mode='same' argument:     {result}")

# using mode='valid' argument
result = np.convolve(actualBuffer, weight, mode='valid')
print(f"using mode='valid' argument:    {result}")


# My implementation of convolve
def myConvolve(actBuffer, weight, mode='full'):
    if mode== 'full':
        tailing = np.zeros(int(weight.size/2)+1)
        actualBuffer = np.concatenate((tailing, actBuffer ,tailing), axis=0)
        result = np.zeros(actBuffer.size+2*int(weight.size/2))
        for i in range(0, actualBuffer.size-weight.size+1):
            for j in range(0, weight.size):
                result[i] += actualBuffer[i+j]*weight[j] 

    if mode== 'same':
        result = np.zeros(actualBuffer.size-int(weight.size/2))

    if mode== 'valid':
        result = np.zeros(actualBuffer.size-2*int(weight.size/2))


    return result
    

print("Result:     ", myConvolve(actualBuffer, weight, mode='full'))