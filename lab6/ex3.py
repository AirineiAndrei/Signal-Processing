import matplotlib.pyplot as plt
import numpy as np 

A = 1
f = 100
faza = 0
Nw = 200
sample = 1000
semnal = lambda x : A * np.sin(2 * np.pi * f * x + faza)

t = np.arange(0,Nw/sample,1/sample)
x = semnal(t)


def box(N):
    return np.ones(N) 
def hamming(N):
    return np.array([1/2 * (1 - np.cos(2 * np.pi * n / N)) for n in range(N)])


fig, axs = plt.subplots(3)

axs[0].plot(t,x)
axs[1].plot(x * box(Nw))
axs[2].plot(x * hamming(Nw))

plt.show()


