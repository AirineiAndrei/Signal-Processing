import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,1,1000)

mysin = lambda x : 6 * np.sin(2 * np.pi * 10 * x + np.pi)
mycos = lambda x : 6 * np.cos(2 * np.pi * 10 * x + np.pi - np.pi/2) #defazat cu pi/2

fig, axs = plt.subplots(2)
axs[0].plot(x,mysin(x))
axs[1].plot(x,mycos(x))

plt.show()