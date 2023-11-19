import matplotlib.pyplot as plt
import numpy as np

N = 10

p = np.random.randint(-1000,1000,np.random.randint(1,N))
q = np.random.randint(-1000,1000,np.random.randint(1,N))

deg_out = len(p) + len(q)
mul_naive = [0 for _ in range(deg_out - 1)]

for (i,coef_i) in enumerate(p):
    for (j,coef_j) in enumerate(q):
        mul_naive[i + j] += coef_i * coef_j

p_fft = np.fft.fft(p,deg_out)
q_fft = np.fft.fft(q,deg_out)

mul_fft = np.real(np.fft.ifft(p_fft*q_fft))[:-1]

mul_conv = np.convolve(p,q)

print(mul_conv)
print(mul_naive)
print(mul_fft)

def test_error(a,b):
    dif = a - b
    err = np.linalg.norm(dif)
    print(f"error is: {err}")
    assert err < 1e-9

test_error(mul_conv,mul_naive)
test_error(mul_conv,mul_fft)
test_error(mul_naive,mul_fft) 
