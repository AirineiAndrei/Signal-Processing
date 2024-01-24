import numpy as np  
import matplotlib.pyplot as plt


INTERVAL = (-1,1)
SAMPLES = 500

x = np.linspace(INTERVAL[0],INTERVAL[1], SAMPLES)
y = np.linspace(INTERVAL[0],INTERVAL[1], SAMPLES)
X, Y = np.meshgrid(x, y)

kernels = {
    "linear"            : lambda x, y                      : x * y,
    "brownian"          : lambda x, y                      : min(x, y),
    "sq exp"            : lambda x, y, alpha = 9           : np.exp(-alpha * np.linalg.norm(x - y) ** 2),
    "Ornstein-Uhlenbeck": lambda x, y, alpha = 15          : np.exp(-alpha * np.abs(x - y)),
    "periodic"          : lambda x, y, alpha = 4, beta = 7 : np.exp(-alpha * np.sin(beta * np.pi * (x - y)) ** 2),
    "simetric"          : lambda x, y, alpha = 27          : np.exp(-alpha * (min(np.abs(x - y), np.abs(x + y))) ** 2)
}

kernel_runs = {
    "linear": 7,
    "brownian": 3,
    "sq exp": 3,
    "Ornstein-Uhlenbeck": 2,
    "periodic": 2,
    "simetric": 2,
}



if __name__ == '__main__':
    for name, kernel in kernels.items():
        plt.figure()
        
        for run in range(kernel_runs[name]):
            print(f'Running {name}, iteration {run+1}')

            cov = np.array([[kernel(x, y) for x, y in zip(xi, yi)] for xi, yi in zip(X, Y)])
            mean = np.zeros(SAMPLES)
            samples = np.random.multivariate_normal(mean, cov)

            plt.plot(x, samples, label=f'Iteration {run+1}')

        plt.title(f'Samples from {name} Kernel')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.legend()

        plt.savefig(f'./results/ex2_{name}_kernel_samples.pdf')
        #plt.show()