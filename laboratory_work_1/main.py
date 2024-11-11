import numpy as np
import matplotlib.pyplot as plt
import my_plot as my_plt
import my_pow_funcs as pf
import my_mashin_func as mf


#Eps = np.finfo(np.double).eps

def relative_error(x0, x):
    err = np.abs(x0 - x) / abs(x0)

    return err
     
class LogNumber(object):
    def __init__(self, zeta):
        self.zeta=zeta
    def __str__(self):
        return "{}".format(self.to_float())
    @staticmethod
    def from_float(x):
        return LogNumber(np.log(x))
    def to_float(self):
        return np.exp(self.zeta)
    def __pow__(self, power):
        return LogNumber(power*self.zeta)
    
x0=np.logspace(-4,4,100,dtype=np.double)
x=(pf.f_sqrt_sqr(LogNumber.from_float(x0))).to_float()
err=relative_error(x0, x)
my_plt.plot_error_loglog(x0, err) 

# create all data+
x0 = np.logspace(-4, 4, dtype = np.double)

x = pf.make_many_sqrt_pow_by_log(x0, 52)
err = relative_error(x0, x)

# do mashin exisate
xs = np.linspace(-1000,1000, 1000)
lse = mf.my_LSE(xs)
lse_der = mf.my_LSE_der(xs)

# plotting results
my_plt.plot_error_loglog(x0, err)
#my_plt.plot_LSE(xs, lse)
#my_plt.plot_LSE_der(xs, lse_der)
