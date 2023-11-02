import matplotlib.pyplot as plt
import numpy as np 
import math
import time

semnal = lambda x : 2 * np.sin(2 * np.pi * x * 3) + 0.5 * np.sin(2 * np.pi * x * 10 + np.pi / 3) + 1.5 * np.sin(2 * np.pi * x * 15 + 7 * np.pi / 5)

def myFourier(N):
    global semnal
    F = np.array([[(math.e**(-2*math.pi*1j*k*m/N)) for k in range(N)] for m in range(N)])
    t = np.linspace(0,1,N)
    x = semnal(t)
    return np.dot(F,x)

def useNumpy(N):
    t = np.linspace(0,1,N)
    x = semnal(t)
    return np.fft.fft(x)

mydft = []
npfft = []

dimensions = [128, 256, 512, 1024, 2048, 4096, 8192,8192*2]

for N in dimensions:
    start = time.time()
    myFourier(N)
    myDuration = time.time() - start

    start = time.time()
    useNumpy(N)
    end = time.time()
    npDuration = end - start

    mydft.append(myDuration)
    npfft.append(npDuration)
    
    print(f"My dft for N={N} {myDuration}  //  numpy fft {npDuration}")

plt.plot(dimensions,mydft)
plt.plot(dimensions,npfft)
plt.yscale('log')
plt.show()