import numpy as np 
import matplotlib.pyplot as plt


samplesize = 2000
t = np.linspace(0,1,samplesize)


semnal1 = lambda x : np.sin(2 * np.pi * 4 * x + np.pi)
semnal2 = lambda x : np.sin(2 * np.pi * 4 * x)
semnal3 = lambda x : np.sin(2 * np.pi * 4 * x + np.pi/2)
semnal4 = lambda x : np.sin(2 * np.pi * 4 * x + 7 * np.pi /3)

semnale = [semnal1,semnal2,semnal3,semnal4]


SNRvals = [0.1,1,10,100]

fig, axs = plt.subplots(4)

# for SNR in SNRvals:
for (indx,fun) in enumerate(semnale):
    x = fun(t)

    z = np.random.normal(0,1,samplesize)
    normz = np.linalg.norm(z)
    normx = np.linalg.norm(x)

    gammasq = (normx ** 2) / ((normz ** 2) * SNRvals[indx])
    gamma = np.sqrt(gammasq)

    x = x + gamma * z

    axs[indx].plot(t,x)

plt.show()