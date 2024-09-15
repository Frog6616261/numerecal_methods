import numpy as np
import matplotlib.pyplot as plt
import my_plot as my_plt
import my_pow_funcs as pf


Eps = np.finfo(np.double).eps

def relative_error(x0, x):
    err = np.abs(x0 - x) / abs(x0)

    return err
     

# create all data
x0 = np.logspace(-4, 4, dtype= np.double)

#x = pf.many_sqrt_pow_by_log(x0, 52, 2)
x = pf.many_pow(x0, 52, 0.5)
x = pf.many_pow(x, 52, 2)
err = relative_error(x0, x)

# plotting results
my_plt.plot_error_loglog(x0, err)
