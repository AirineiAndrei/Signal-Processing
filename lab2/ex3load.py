import numpy as np 
import matplotlib.pyplot as plt
from scipy.io import wavfile

# a
ta = np.linspace(0,1,1600)
signsin = lambda x : np.sin(400 * 2 * np.pi * x)
wavfile.write('a.wav', 1600, signsin(ta))

# b
tb = np.linspace(0,3,1000)
signsinb = lambda x : np.sin(800 * 2 * np.pi * x)
wavfile.write('b.wav', 1000, signsinb(tb))

#c 

tc = np.linspace(0,0.05,2000)
saw = lambda x : np.mod(x,1/240) * 240
wavfile.write('c.wav', 2000, saw(tc))

#d 
td = np.linspace(0,0.05,2000)
square = lambda x : np.sign(np.mod(x,1/300) - 1/600)
wavfile.write('d.wav', 2000, square(td))

