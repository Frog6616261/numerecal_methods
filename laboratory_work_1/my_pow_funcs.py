import numpy as np

Eps = np.finfo(np.double).eps


def make_many_sqrt_pow_by_log(x0, iter = 52):
    y = np.log(x0)

    #for k in range(iter):  y = y / 2
    #for k in range(iter):  y = y * 2

    y = y / (2**52)
    y = y * (2**52)

    x = np.exp(y)

    return x

def f_sqrt_sqr(x, n=52):
    for k in range(n): x=x**0.5
    for k in range(n): x=x**2
    return x




