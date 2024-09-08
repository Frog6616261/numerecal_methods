import numpy as np
import matplotlib.pyplot as plt
import my_plot as my_plt


Eps = np.finfo(np.double).eps

def relative_error(x0, x):
    long = len(x0)
    err = [0.0]*long
    for k in range(0, long):
        x_k = x[k]
        x0_k = x0[k]
        err[k] = np.abs(x_k - x0_k)/np.abs(x0_k)
    return err


def my_pow(x, numb_pow):
    return np.pow(x, numb_pow) * (1 + numb_pow*Eps)

def f_sqrt_sqr(x, iter = 52):
    for k in range(iter): my_pow(x, 0.5)
    for k in range(iter): my_pow(x, 2)

    return x    

# create all data
x0 = np.logspace(-4, 4, dtype= np.double)
x = f_sqrt_sqr(x0)
err = relative_error(x0, x)

# plotting results
my_plt.plot_error_linlin(x0, err)
