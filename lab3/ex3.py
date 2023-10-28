
import matplotlib.pyplot as plt
import numpy as np 
import math

N = 1000
t = np.linspace(0,1,N)
semnal = lambda x : 2 * np.sin(2 * np.pi * x * 3) + 0.5 * np.sin(2 * np.pi * x * 10 + np.pi / 3) + 1.5 * np.sin(2 * np.pi * x * 15 + 7 * np.pi / 5)

x = semnal(t)

fig, axs = plt.subplots(2)

axs[0].plot(t,x)


def moduleFourier(omega):
    global x,N
    fourier = [xn * (math.e**(-2*math.pi*1j*omega *indx/N)) for indx,xn in enumerate(x)]
    return abs(sum(fourier))

print(f"module of fourier for {3} is {moduleFourier(3)}")



for i in range(0,50):
    axs[1].stem(i,moduleFourier(i))

plt.show()