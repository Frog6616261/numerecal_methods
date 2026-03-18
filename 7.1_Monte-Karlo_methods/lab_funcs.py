import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import math

def get_abs_err(x, x0):
    return np.abs(x - x0)

def get_relative_err(x, x0):
    return np.abs(x - x0) / np.abs(x0)

