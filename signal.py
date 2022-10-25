import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,7,1)
y=np.sin(6*np.pi*t)+np.cos(5*np.pi*t)

plt.plot(t,y)
plt.title("T as integers")
plt.xlabel("T")
plt.ylabel("x(T)")