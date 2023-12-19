import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA


N=1000
t = np.linspace(0,1,N)
#a
trend = lambda x : 20 * x ** 2 - 9 * x + 123
sezon = lambda x : np.sin(2 * np.pi * x) + np.sin(2 * np.pi * x * 5)
noise = np.random.normal(0,1,N) / 2
serie = trend(t) + sezon(t) + noise

balpha = 0

#b 
def EMA(alpha):
    exponential_average = [serie[0]]
    for i in range(1, len(serie) - 1):
        next_average = alpha * serie[i] + (1 - alpha) * exponential_average[i-1]
        exponential_average.append(next_average)
    
    return exponential_average

berror = np.Infinity
errs = []

for alpha in np.arange(0,1,0.001):
    em = EMA(alpha)
    error = mean_squared_error(em,serie[1:])
    # print(f"for alpha={alpha} error is  {error}")
    errs.append(error)
    if error < berror:
        berror = error
        balpha = alpha

plt.yscale('log')
plt.plot(errs)
plt.show()

print(f"best alpha is {balpha}")
exponential_average = EMA(balpha)
plt.plot(t,serie)
plt.plot(t[1:],exponential_average)
plt.show()


# c
 
 #????


# d
train_amount = (N * 9) // 10
train = serie[:train_amount]
test = serie[train_amount:]

q = 10

history = list(train.copy())
pred = list()

# https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
print(train_amount)
for tst in range(len(test)):
    model = ARIMA(history, order=(5,1,0))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    pred.append(yhat)
    obs = test[tst]
    history.append(obs)
    # print('predicted=%f, expected=%f' % (yhat, obs))


plt.plot(t,serie)    
plt.plot(t[train_amount:],pred)
plt.show()

