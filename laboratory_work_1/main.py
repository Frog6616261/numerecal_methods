import numpy as np
import matplotlib.pyplot as plt
import my_plot as my_plt


Eps = np.finfo(np.double).eps

def relative_error(x0, x):
    err = np.abs(x0- x) / abs(x0)

    return err


def my_pow(x, numb_pow):
    return np.pow(x, numb_pow) * (1 + numb_pow*Eps) + Eps

def f_sqrt_sqr(x, iter = 52):
    for k in range(iter): x = my_pow(x, 0.5)
    for k in range(iter): x = my_pow(x, 2)

    return x 

def f_sqrt_sqr_err(x, iter = 52):
    for k in range(iter): x = np.pow(x, 0.5)
    for k in range(iter): x = np.pow(x, 2)

    return x       

# create all data
x0 = np.logspace(-4, 4, dtype= np.double)
x = f_sqrt_sqr(x0)
err = relative_error(x0, x)

# plotting results
my_plt.plot_error_loglog(x0, err)
