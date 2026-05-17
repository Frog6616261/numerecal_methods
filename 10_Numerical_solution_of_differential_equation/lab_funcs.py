import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import math


def get_abs_err(x, x0):
    return np.abs(x - x0)

def get_rel_err(x, x0):
    return np.abs(x - x0) / np.abs(x0)


def get_mse_err(x_est, x_true, axis=0):
    """
    Среднеквадратичная ошибка (MSE)
    """
    err = x_est - x_true
    return np.mean(err**2, axis=axis)


def get_rmse_err(x_est, x_true, axis=0):
    """
    Корень из MSE (RMSE)
    """
    return np.sqrt(get_mse_err(x_est, x_true, axis=axis))

def get_mse_rel_err(x_est, x_true, axis=0):
    """
    Среднеквадратичная относительная ошибка
    """
    rel_err = get_rel_err(x_est, x_true)
    return np.mean(rel_err**2, axis=axis)


def get_rmse_rel_err(x_est, x_true, axis=0):
    """
    RMS относительной ошибки (то, что тебе нужно)
    """
    return np.sqrt(get_mse_rel_err(x_est, x_true, axis=axis))