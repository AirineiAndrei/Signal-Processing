import numpy as np 
import matplotlib.pyplot as plt


f = 1000
t = np.arange(-np.pi / 2,np.pi / 2,1/f)

pade = lambda x : (x - 7 * x ** 3 / 60) / (1 + x ** 2 / 20) 

fig, axs = plt.subplots(4)
axs[0].plot(t,np.sin(t))
axs[0].plot(t,t)

axs[1].plot(t,t - np.sin(t))


axs[2].plot(t,np.sin(t))
axs[2].plot(t,pade(t))

axs[3].plot(t, np.sin(t) - pade(t))

plt.show()