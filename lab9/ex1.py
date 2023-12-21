from functools import lru_cache
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
plt.savefig(f"./result/berr.pdf", format="pdf")
plt.show()

print(f"best alpha is {balpha}")
exponential_average = EMA(balpha)
plt.plot(t,serie)
plt.plot(t[1:],exponential_average)
plt.savefig(f"./result/b.pdf", format="pdf")
plt.show()


# c
 
@lru_cache(maxsize=None)
def get_noise(size):
    return np.random.normal(size=size)

train_amount = (N * 8) // 10
train = serie[:train_amount]
test = serie[train_amount:]
mean = train.mean()


def train_ma(q):
    noise = get_noise(len(train) + q)

    # so we have a system only in theta
    y = train - noise[q:] - mean
    n = y.shape[0]

    errMat = np.zeros((n,q))
    for i in range(n):
        errMat[i] = noise[i+q:i:-1]
    
    theta, _, _, _  = np.linalg.lstsq(errMat,y,rcond=None)
    return theta

def train_predict_ma(q):    
    theta = train_ma(q)

    # print(theta.shape)
    serie_error = get_noise(N + q)
    pred = []
    for i in range(len(test)):
        indx = i + len(train) - 1
        # print(indx,indx + q,serie_error[indx:indx+q].shape)
        yhat = serie_error[indx+q:indx:-1] @ theta
        yhat += mean + serie_error[i]
        pred.append(yhat)
    return np.array(pred)

bq = 0
berror = np.Infinity
errs = []

for q in range(1,500):
    pred = train_predict_ma(q)
    error = mean_squared_error(test,pred)
    # print(f"for q={q} error is  {error}")
    errs.append(error)
    if error < berror:
        berror = error
        bq = q

print(f"best q is {bq} error {berror}")
pred = train_predict_ma(bq)

plt.plot(t,serie)    
plt.plot(t[train_amount:],pred)
plt.savefig(f"./result/c.pdf", format="pdf")
plt.show()



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
plt.savefig(f"./result/d.pdf", format="pdf")

plt.show()

