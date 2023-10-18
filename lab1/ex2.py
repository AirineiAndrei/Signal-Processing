import numpy as np 
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4)
fig.suptitle('Titlu')

# a
ta = np.linspace(0,1,1600)
signsin = lambda x : np.sin(400 * 2 * np.pi * x)
axs[0].plot(ta,signsin(ta))

# b
tb = np.linspace(0,3,200)
signsinb = lambda x : np.sin(800 * 2 * np.pi * x)
axs[1].plot(tb,signsinb(tb))

#c 

tc = np.linspace(0,1,10000)
saw = lambda x : np.mod(x,1/240) * 240
tc = tc[:240]
axs[2].plot(tc,saw(tc))

#d 
td = np.linspace(0,1,10000)
square = lambda x : np.sign(np.mod(x,1/300) - 1/600)

td = td[:300]
axs[3].plot(td,square(td))

plt.show()

#e 
signal2d = np.random.rand(128,128)
plt.imshow(signal2d)
plt.show()

#f
blank = np.zeros((128,128))
blank[50:80] = 1
blank[70:100,20:30] = 0.5
plt.imshow(blank)
plt.show()#picasso
