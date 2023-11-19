import matplotlib.pyplot as plt
import numpy as np

# a
x = np.genfromtxt('../lab5/Train.csv', delimiter=',')[1:,2][:3 * 24]

# b
w_arr = [1,5,9,13,17]
fig, axs = plt.subplots(len(w_arr))
for indx,w in enumerate(w_arr):
    smooth = np.convolve(x,np.ones(w),'valid')
    axs[indx].plot(smooth)
plt.show()



