import matplotlib.pyplot as plt
import numpy as np 

freq = 5
semnal = lambda x : np.sin(2 * np.pi * x * freq)

esatione = 10
t = np.linspace(0,1,10)

fig, axs = plt.subplots(3)

axs[0].plot(t,semnal(t))


