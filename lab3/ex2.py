import matplotlib.pyplot as plt
import numpy as np 
import math

freq = 5
n = 5000
t = np.linspace(0,1,n)
semnal = lambda x : np.sin(2 * np.pi * freq * x)


fig, axs = plt.subplots(2,figsize=(5, 12))
xn = semnal(t)
axs[0].plot(t,xn)
ftx = [x * (math.e**(-2*math.pi*1j*indx/n))  for indx,x in enumerate(xn)]

real = np.array([x.real for x in ftx])
imag = np.array([x.imag for x in ftx])

dist = np.sqrt(real**2 + imag**2)

axs[1].scatter(real, imag, c=dist, cmap='plasma')

plt.show()


for omega in [1,2,freq,7,10]:
    ftx = [x * (math.e**(-2*math.pi*1j*omega *indx/n)) for indx,x in enumerate(xn)]

    real = np.array([x.real for x in ftx])
    imag = np.array([x.imag for x in ftx])

    dist = np.sqrt(real**2 + imag**2)

    plt.scatter(real, imag, c=dist, cmap='plasma')
    plt.colorbar()
    plt.show()

