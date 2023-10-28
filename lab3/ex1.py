import matplotlib.pyplot as plt
import numpy as np 
import math

N = 8
F = np.array([[(math.e**(-2*math.pi*1j*k*m/N)) for k in range(N)] for m in range(N)])

Freal = [[x.real for x in line] for line in F]
Fimag = [[x.imag for x in line] for line in F]


fig, axs = plt.subplots(16,figsize=(6,50))

for i,(real,imag) in enumerate(zip(Freal,Fimag)):
    axs[2 * i].stem(real,'r')
    axs[2 * i + 1].stem(imag,'g')
    
plt.show()

Fh = np.array([[x.real - 1j*x.imag for x in line] for line in F.T])

test = np.dot(F,Fh) -  N * np.identity(N)
error = np.linalg.norm(test)
print(test)

assert error < 1e-6
print(f"Error is {error}") # ~ 2e-14

