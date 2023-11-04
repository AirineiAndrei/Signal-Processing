import matplotlib.pyplot as plt
import numpy as np 

freq = 2
esatione = 10 # cu 10 avem aliasing, cu 50 nu avem
semnal = lambda x : np.sin(2 * np.pi * x * 2)
semnal1 = lambda x : np.sin(2 * np.pi * x * 12)
semnal2 = lambda x : np.sin(2 * np.pi * x * 22)

t = np.linspace(0,1,esatione + 1)
t_desen = np.linspace(0,1,1000)

fig, axs = plt.subplots(3)

axs[0].plot(t_desen,semnal(t_desen))
axs[0].stem(t,semnal(t))

axs[1].plot(t_desen,semnal1(t_desen))
axs[1].stem(t,semnal(t))

axs[2].plot(t_desen,semnal2(t_desen))
axs[2].stem(t,semnal(t))

plt.show()


