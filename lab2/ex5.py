import numpy as np 
import matplotlib.pyplot as plt
from scipy.io import wavfile

fig, axs = plt.subplots(3)
rate = 4000
t = np.linspace(0,2,rate)

sin1 = lambda x : np.sin(2 * np.pi * x * 400) # e mai jos
sin2 = lambda x : np.sin(2 * np.pi * x * 1000) # e foarte sus, ma dor urechile

x = np.append(sin1(t),sin2(t))
print(x.shape)
wavfile.write('ex5.wav', 2000, x)
