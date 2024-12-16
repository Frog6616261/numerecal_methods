
import numpy as np
import matplotlib.pyplot as plt

def relative_error(x0,x):
    return np.abs(x0-x)/np.abs(x0)