import numpy as np 
import matplotlib.pyplot as plt

fs = 100
t = np.linspace(0,1,fs)

sin1 = lambda x : np.sin(2 * np.pi * x * fs / 2)
sin2 = lambda x : np.sin(2 * np.pi * x * fs)
sin3 = lambda x : np.sin(2 * np.pi * x * 0)

fig, axs = plt.subplots(3)

axs[0].plot(t,sin1(t)) # forma ciudata, ca doua jumatati de con aplatizate
axs[1].plot(t,sin2(t)) # sin normal
axs[2].plot(t,sin3(t)) # linie dreapta

plt.show()
