import matplotlib.pyplot as plt
import numpy as np

eps = np.finfo(np.double).eps

def plot_error_loglog(x0, err):
    mask=np.logical_and(err>0,err<np.inf)
    plt.loglog(x0[mask],err[mask],".k")
    plt.loglog(x0,[eps]*len(err),"--r") # машинная точность для сравнения
    plt.xlabel("$Значение\;аргумента$")
    plt.ylabel("$Относительная\;погрешность$")
    plt.show()

def plot_error_linlin(x0, err):
    plt.plot(x0, err, 'ro')
    plt.plot(x0,[eps]*len(err),"--r") # машинная точность для сравнения
    plt.xlabel("$Значение\;аргумента$")
    plt.ylabel("$Относительная\;погрешность$")
    plt.show()


def plot_LSE(x_LSE, LSE):
    
    plt.plot(x_LSE, LSE)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.show()

def plot_LSE_der(x_LSE_der, LSE_der):
    
    plt.plot(x_LSE_der, LSE_der)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.show()

