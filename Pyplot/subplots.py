import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])

plt.subplot(212)             # the second subplot in the first figure
plt.plot([6, 5, 3])



plt.figure(2)                # a second figure
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

#Subplot 221
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.title('Easy as 1, 2, 3') 

# Subplot 222
plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.text(2.5, 0, 'subplot(224) background text', ha='center', va='center', size=10, alpha=.5)


# Subplot 223
plt.subplot(223) 
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)              

# Subplot 224
plt.subplot(224)
plt.text(0.5, 0.5, 'subplot(224) could be here', ha='center', va='center', size=12, alpha=.5)


plt.figure(1) # Make figure in front og figure 2

plt.show()

