import numpy as np 
import matplotlib.pyplot as plt


start = 0
end = 0.03
# a
t = np.arange(start,end,0.0005)

x = lambda t : np.cos(520 * np.pi * t + np.pi / 3)
y = lambda t : np.cos(280 * np.pi * t - np.pi / 3)
z = lambda t : np.cos(120 * np.pi * t + np.pi / 3)

# b
fig, axs = plt.subplots(3)
fig.suptitle('Titlu')
axs[0].plot(t,x(t))
axs[1].plot(t,y(t))
axs[2].plot(t,z(t))

# plt.show()
#c 

tt = np.linspace(start,end,int((end-start)*200))

# fig, axs = plt.subplots(3)
# fig.suptitle('Titlu')
axs[0].stem(tt,x(tt))
axs[1].stem(tt,y(tt))
axs[2].stem(tt,z(tt))

plt.show()
