import numpy as np
import matplotlib.pyplot as plt

# параметры выборки
mean=1e5 # среднее
delta=1e-6 # величина отклонения от среднего

def get_mean():
    return mean

def get_delta():
    return delta

def relative_error(x0, x):
    """Погрешность x при точном значении x0"""
    return np.abs(x0-x)/np.abs(x)

def Kahan_sum(x):
    s=0.0 # частичная сумма
    c=0.0 # сумма погрешностей
    for i in x:
        y=i-c      # первоначально y равно следующему элементу последовательности
        t=s+y      # сумма s может быть велика, поэтому младшие биты y будут потеряны
        c=(t-s)-y  # (t-s) отбрасывает старшие биты, вычитание y восстанавливает младшие биты
        s=t        # новое значение старших битов суммы
    return s

def direct_sum(x):
    s=0.
    for e in x:
        s+=e
    return s

def samples(N_over_two):
    """Генерирует выборку из 2*N_over_two значений с данным средним и среднеквадратическим
    отклонением."""
    x=np.full((2*N_over_two,), mean, dtype=np.double)
    x[:N_over_two]+=delta
    x[N_over_two:]-=delta
    return np.random.permutation(x)

def array_samples(N_max):
    x = [samples(k) for k in range(1, N_max+1)]
    return x

def exact_mean():
    """Значение среднего арифметического по выборке с близкой к машинной точностью."""
    return mean

def exact_variance():
    """Значение оценки дисперсии с близкой к машинной точностью."""
    return delta**2

def direct_mean(x):
    """Среднее через последовательное суммирование."""
    a = direct_sum(x)/len(x)
    return a

def direct_second_var(x):
    """Вторая оценка дисперсии через последовательное суммирование."""
    a = direct_mean(x**2)
    b = ((direct_mean(x))**2)
    return a - b

def online_second_var(x):
    """Вторая оценка дисперсии через один проход по выборке"""
    m=x[0] # накопленное среднее
    m2=x[0]**2 # накопленное среднее квадратов
    for n in range(1,len(x)):
        m=(m*(n-1)+x[n])/n
        m2=(m2*(n-1)+x[n]**2)/n
    return m2-m**2

def oneline_first_var(x):
    """Первая оценка дисперсии через один проход по выборке"""
    m = x[0] # накопленное среднее
    m_prev = x[0] # накопленное среднее на предыдущем шаге
    d = 0 # накопленная дисперсия
    for n in range(1,len(x)):
        m_prev = m
        m = (m*(n - 1) + x[n])/n
        d = (n-1)/(n)*d + 1/n * (x[n] - m)*(x[n] - m_prev)
    return d

def direct_first_var(x):
    """Первая оценка дисперсии через последовательное суммирование."""
    b = x-direct_mean(x)
    d = b**2
    c = direct_mean(d)
    return c

