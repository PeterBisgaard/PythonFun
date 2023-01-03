#Examples from https://matplotlib.org/stable/tutorials/introductory/pyplot.html

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled 0-1 with 0.1 intervals = 10 numbers
t = np.arange(0., 1., 0.1)

# red dots, blue squares and green triangles
plt.plot(t, t, 'ro', t, t**2, 'bs', t, t**3, 'g^', t,t**4,'y-')
# add a nother data set format in the same plot 
plt.plot([0.1, 0.3, 0.5, 0.75], [0.4,0.2 , 0.9, 1], 'r--')

# add labels
plt.title('Plotting with Matplotlib')
plt.ylabel('0.2 intervals')
plt.xlabel('Numbers between 0 and 1')

plt.show()