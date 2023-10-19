import numpy as np 
import matplotlib.pyplot as plt


f = 1000
t = np.arange(0,1,1/f)

semnal = lambda x : np.sin(2 * np.pi * x * 5)


tdeci = t[::4] # every 4th from the begining
tdeci2 = t[1::4] # every 4th starting with second

print(t.shape,tdeci.shape)

fig, axs = plt.subplots(3)

axs[0].plot(t,semnal(t))
axs[1].plot(tdeci,semnal(tdeci))
axs[2].plot(tdeci2,semnal(tdeci2))

#nu observ o diferenta cu ochil liber

plt.show()