import numpy as np  
import matplotlib.pyplot as plt


def my_normal(mu,sigma,size):
    return mu + np.sqrt(sigma) * np.random.normal(size=size)

tst = my_normal(2,5,10000)
print(np.mean(tst),np.var(tst))
plt.hist(tst,bins=100)
plt.savefig('./results/ex1_1d.pdf', format='pdf')
plt.show()

# gaussian 2d

SIGMA = [
    [1,3/5],
    [3/5,2]
]
MIU = [0,0]

def sample_gaussian_2d():
    global SIGMA, MIU
    values, vectors = np.linalg.eig(SIGMA)
    sqrt_lamb = np.array([
        [np.sqrt(values[0]) , 0                 ],
        [0                  , np.sqrt(values[1])]
    ])
    u = vectors
    n = np.random.normal(size=2)

    return u @ sqrt_lamb @ n + MIU

def gaussian_2d_pdf(x, y):
    xy = np.array([x, y])
    part1 = 1 / (2 * np.pi * np.sqrt(np.linalg.det(SIGMA)))
    part2 = np.exp(-0.5 * (xy - MIU).T @ np.linalg.inv(SIGMA) @ (xy - MIU))
    return part1 * part2

samples = np.array([sample_gaussian_2d() for _ in range(10000)])

# Plotting
plt.figure(figsize=(8, 8))
plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5)

# Contour
x = np.linspace(min(samples[:, 0]), max(samples[:, 0]), 100)
y = np.linspace(min(samples[:, 1]), max(samples[:, 1]), 100)
X, Y = np.meshgrid(x, y)
Z = np.array([[gaussian_2d_pdf(x, y) for x, y in zip(xi, yi)] for xi, yi in zip(X, Y)])
plt.contour(X, Y, Z)

plt.title('2D Gaussian Distribution Samples with Contour')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.axis('equal')
plt.savefig('./results/ex1_2d.pdf', format='pdf')
plt.show()


