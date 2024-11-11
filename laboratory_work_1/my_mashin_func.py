import numpy as np

Eps = np.finfo(np.double).eps

def my_LSE(x):

    long = len(x)
    result = np.linspace(-1000,1000, long)

    for k in range(0,long):
        if x[k]>700:
            result[k] = x[k]
        else:
            result[k] = np.log(1 + np.exp(x[k]))
    
    return result

def my_LSE_der(x):

    long = len(x)
    result = np.linspace(-1000,1000, long)

    for k in range(0,long):
        if x[k]>700:
            result[k] = 1
        else:
            result[k] = np.exp(x[k]) / (1 + np.exp(x[k]))
    
    return result




