# Help from: 
#   https://www.w3schools.com/python/numpy/numpy_array_filter.asp for filter functionality
#   https://www.statology.org/numpy-count/ for counting functionality

#   What is differens between or and | in python?
#   https://www.w3schools.com/python/python_operators.asp



import numpy as np

samples = np.array([1.3, 2.2, 2.3, 4.2, 5.1, 3.2, 5.3, 3.3, 2.1, 1.1, 5.2, 3.1])
print('Samples:          ',samples)

# Create a fileter array
filter_arr = []

# For each id in samples
for id in samples:
    # Check if 3 occurences x.1 or x.2 or x.3 exists for each id
    if np.count_nonzero((samples == int(id)+0.1) | (samples == int(id)+0.2) | (samples == int(id)+0.3)) == 3:
        filter_arr.append(True)
    else:
        filter_arr.append(False)


newarr = samples[filter_arr]
print('Filter:           ', filter_arr)
print('Filtered samples: ',newarr)
