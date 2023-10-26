import matplotlib.pyplot as plt
import numpy as np 
import math

N = 8
F = np.array([[(math.e**(-2*math.pi*1j*k*m/N)) for k in range(N)] for m in range(N)])

Freal = [[x.real for x in line] for line in F]
Fimag = [[x.imag for x in line] for line in F]


# for real,imag in zip(Freal,Fimag):
#     fig, axs = plt.subplots(2)
#     axs[0].stem(real)
#     axs[1].stem(imag)
#     plt.show()

Fh = np.array([[x.real - 1j*x.imag for x in line] for line in F.T])

test = np.dot(F,Fh) -  N * np.identity(N)
error = np.linalg.norm(test)
print(test)
print(f"Error is {error}")

