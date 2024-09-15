import numpy as np

Eps = np.finfo(np.double).eps

def many_pow_by_log(x, iter = 52, pow_numb = 2):
    y = np.log(x)
    y = y * (pow_numb**iter)
    x = np.exp(y)
    return x

def many_sqrt_pow_by_log(x, iter = 52, pow_numb = 2):
    y = np.log(x) + Eps
    y = y / (pow_numb**iter) + Eps*np.abs(y / (pow_numb**iter))
    x = np.exp(y) + np.exp(y)*np.abs(y)*Eps
    return x

def many_pow(x, iter = 52, pow_numb = 2):
    for k in range(iter): x = my_pow(x, pow_numb)
    return x


def my_pow(x, pow_numb):
    return np.pow(x, pow_numb) + np.pow(x, pow_numb)*pow_numb*Eps


