import matplotlib.pyplot as plt
import numpy as np

x = np.random.random(100)

fig, axs = plt.subplots(4)

for iter in range(4):
    axs[iter].plot(x)
    x = x * x

plt.show()
# spike-uile sunt mult mai accentuate deoare restul valorilor se apropie de 0 datorita inmultirii
