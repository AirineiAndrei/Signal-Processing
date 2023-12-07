import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

N=1000
t = np.linspace(0,1,N)
#a
trend = lambda x : 20 * x ** 2 - 9 * x + 123
sezon = lambda x : np.sin(2 * np.pi * x) + np.sin(2 * np.pi * x * 5)
noise = np.random.normal(0,1,N) / 2
serie = trend(t) + sezon(t) + noise

fig, axs = plt.subplots(4)
axs[0].plot(t,trend(t))
axs[1].plot(t,sezon(t))
axs[2].plot(t,noise)
axs[3].plot(t,serie)
plt.show()

#b
autocorr = np.correlate(serie,serie,mode="full")
autocorr = autocorr[autocorr.size // 2:]
plt.plot(autocorr)
plt.show()

berror = np.Infinity
bprediciton = ()
bestp = 2

m = 900
start = m + 1
train = serie[:m]
for p in range(2,50):
    def AR(y,p):
        Y = np.array([[y[i - j - 1] for j in range(p)] for i in range(m)])
        # print(y.shape,Y.shape)
        Ycross=np.matmul(np.linalg.inv(np.matmul(Y.T, Y)),Y.T)
        # print(Ycross.shape)
        xstar = np.matmul(Ycross,y[-m:])
        # print(xstar)
        return xstar.T
    x = AR(train,p)
    print(x)

    predictions = [np.matmul(x,serie[i - p - 1:i - 1]) for i in range(start,N)]
    actual = serie[start:]
    error = mean_squared_error(actual,predictions)
    print(f"iter error {error}")
    if error < berror:
        berror = error
        bestp = p
        bprediciton = predictions

print(f"best is {bestp}")

plt.plot(t[start:],serie[start:])
plt.plot(t[start:],bprediciton)
plt.show()
