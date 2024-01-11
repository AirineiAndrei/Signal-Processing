import numpy as np  
import matplotlib.pyplot as plt


def my_normal(mu,sigma,size):
    return mu + np.sqrt(sigma) * np.random.normal(size=size)

tst = my_normal(2,5,10000)
print(np.mean(tst),np.var(tst))
# plt.hist(tst,bins=100)
# plt.show()

# gaussian 2d

sigma = [
    [1,3/5],
    [3/5,2]
]


