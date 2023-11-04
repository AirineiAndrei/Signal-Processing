import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read

fs, data = read("ex6-vocale.wav")

data = data[:(len(data)//200) * 200]
groupsize = len(data) // 200

groups = np.array([data[x:x+groupsize] for x in range(0,len(data),len(data)//200)])

ffts = np.array([10 * np.log(np.abs(np.fft.fft(x))) for x in groups]).T

plt.figure(figsize=(10,2))
plt.imshow(ffts, aspect='auto',cmap='plasma')
plt.show()
