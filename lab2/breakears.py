import numpy as np
import sounddevice as sd
from scipy.io import wavfile

rate = int(10e5)
fs = 44100  # standard sample rate for audio
t = np.linspace(0, 10, fs)  
y = np.sin(2 * np.pi * 440 * t)


wavfile.write('nume.wav', fs, y)


_, read_y = wavfile.read('nume.wav')

# Play the signal
sd.play(read_y, fs)
sd.wait()  
