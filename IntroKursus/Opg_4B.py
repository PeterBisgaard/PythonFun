import numpy as np

def computeItemCost(resourceItemMatrix, resourceCost):
    print("Resource item matrix:\n",resourceItemMatrix)
    print("Resource cost matrix:\n", resourceCost)

    # Insert your code here
    itemCost = np.zeros(resourceItemMatrix.shape[1])    # create an array of zeros with the same length as the number of columns in the resourceItemMatrix

    for i in range(resourceItemMatrix.shape[1]):        # loop through the shape[1] (columns) of the resourceItemMatrix
        for j in range(resourceItemMatrix.shape[0]):    # loop through the shape[0] (rows) of the resourceItemMatrix
            itemCost[i] += resourceItemMatrix[j,i] * resourceCost[j]    # multiply the value in the resourceItemMatrix with the corresponding value in the resourceCost array and add it to the itemCost array
    return itemCost



print(computeItemCost(np.array([[6,3,0],[17,11,9],[4,2,12]]), np.array([101.25,84.00,75.50])))