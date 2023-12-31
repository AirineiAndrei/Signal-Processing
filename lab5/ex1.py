import matplotlib.pyplot as plt
import numpy as np

x = np.genfromtxt('Train.csv', delimiter=',')[1:,2]

# a - este esantionat la interval de o ora, 1/3600 Hz
Fs = 1 / (60 * 60)
# b - 25-08-2012 00:00 - 25-09-2014 23:00 -- 2 ani si o luna
# c fv maxim  1 / 3600 / 2 = 1 / 7200

# d

def do_fft(x):
    N = len(x)
    X = np.fft.fft(x)
    X = np.abs(X/N)
    X = X[:N//2]
    f = Fs*np.linspace(0,N/2,N//2)/N

    plt.plot(f,X)
    plt.show()
    return (f,X)

# e 

(f,X) = do_fft(x)
print(f"fft in 0: {X[0]}")
# modulul transformatei are o valoare semnificativa pentru frecvent, a 0Hz.
# centrare in 0
x -= np.average(x)
(f,X) = do_fft(x)
print(f"fft in 0 after centrare: {X[0]}")

topcnt = 5
indxmax = np.argsort(X)[-topcnt:][::-1]
top = f[indxmax]
print(*top)
print(X[indxmax])


print(top * (60 * 60 * 24 * 365)) 
# putem vedea peridicitate pe zile, an si cea rezultata din fft pt ca analizam pe 2 ani
# si o periodicitate la 1/3 din perioada 8 luni? cel mai posibil anul scolar?
# daca extindem la top 5 gasim si frecventa pt saptamani

start = 6602
onemonth = x[start:start + 24 * 30]
#h

#presupun ca avem niste date in timp legate de variati traficului in timp, ie freceventele data de fft pe tot semnalul de 2 ani
# ne putem da seama de perioada din an din care face parte semnalul din frecventa analizand cum se modifica acesta pe parcursul anului
# alternativ putem incerca sa facem mai multe potriviri la diferite perioade din frecventele dominante
# daca avem tot semnalul de baza putem vedea de unde e aceasta subsec 

plt.plot(onemonth)
plt.show()
# i

x = onemonth
N = len(x)
X = np.fft.fft(x)

f = Fs*np.linspace(0,N/2,N//2)/N
print(f[-20:])
bound = 1 / (60 * 60 * 24) #filtrez frecventele la nivel de zile, semnalul va fii mai smooth dar va urma aprox aceiasi forma
print(bound)
cutoff =  np.argmax(f > bound)
X[cutoff:-cutoff] = 0

filtered = np.fft.ifft(X)
plt.plot(x)
plt.plot(filtered)
plt.show()

