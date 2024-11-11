import matplotlib.pyplot as plt
import numpy as np



def plot_err_f_and_s(err_f, err_s, N_val):
    plt.plot(err_f, N_val, 'ro')
    plt.plot(err_s, N_val, "--r") 
    plt.xlabel("кол-во значений")
    plt.ylabel("$Относительная\;погрешность$")
    plt.show()


