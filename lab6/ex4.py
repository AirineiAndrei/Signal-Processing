import matplotlib.pyplot as plt
import numpy as np
import scipy

# a
x = np.genfromtxt('../lab5/Train.csv', delimiter=',')[1:,2][:3 * 24]
# b
w_arr = [1,5,9,13,17]
fig, axs = plt.subplots(len(w_arr))
for indx,w in enumerate(w_arr):
    smooth = np.convolve(x,np.ones(w),'valid')
    axs[indx].plot(smooth)
plt.savefig(f'./results/ex4b.png',format='png')
plt.savefig(f'./results/ex4b.pdf',format='pdf')
plt.close()

#c 
# frecventa de esantionare este 1 data pe ora deci 1/3600 Hertz
# frecventa Nyquist este 2 * frecv_esantionare deci 1/1800 hertz
# alegem cutoff sa fie la 3/4 din frecventa Nyquist deci 3 / 4 * 1800 -> 1 / 2400 || deci 3/4 Niquist
cutoff = 3 / 4

#d 
def show_butter(N):
    butter_b, butter_a = scipy.signal.butter(N, cutoff)

    #e  # as alege cheby, pare sa arate mai 'human readable' trendurile in trafic
    x_butter = scipy.signal.filtfilt(butter_b,butter_a,x)

    plt.plot(x)
    plt.plot(x_butter)
    
    plt.savefig(f'./results/butter_N={N}.png',format='png')
    plt.savefig(f'./results/butter_N={N}.pdf',format='pdf')
    plt.close()

def show_cheby(N,rb):
    checby_b ,cheby_a = scipy.signal.cheby1(N, rb, cutoff)
    x_cheby = scipy.signal.filtfilt(checby_b,cheby_a,x)

    plt.plot(x)
    plt.plot(x_cheby)
    
    plt.savefig(f'./results/cheby_N={N}_rb={rb}.png',format='png')
    plt.savefig(f'./results/cheby_N={N}_rb={rb}.pdf',format='pdf')
    plt.close()

# e and f

for N in [1,4,5,6,12]:
    show_butter(N)

for N,rb in [(5,5),(6,5),(4,5),(1,1),(10,10),(1,10),(10,1)]:
    show_cheby(N,rb)

# imi place cel mai mult cum arata cheby cu N=1 si rb=10, aplatizeaza bine spikeruile si overall caputureaza bine crestearea descresterea traficului