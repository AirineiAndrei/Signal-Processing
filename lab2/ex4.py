import numpy as np 
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)

t = np.linspace(0,1,2000)

sin = lambda x : np.sin(2 * np.pi * x * 10)
axs[0].plot(t,sin(t))

saw = lambda x : np.sign(np.sin(2 * np.pi * x * 7))
axs[1].plot(t,saw(t))

sum = lambda x : sin(x) + saw(x)
axs[2].plot(t,sum(t))

plt.show()