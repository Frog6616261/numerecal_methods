import numpy as np
import matplotlib.pyplot as plt

# параметры выборки
mean=1e6 # среднее
delta=1e-5 # величина отклонения от среднего

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
    
    return Kahan_sum(x)

def samples(N_over_two):
    """Генерирует выборку из 2*N_over_two значений с данным средним и среднеквадратическим
    отклонением."""
    x=np.full((2*N_over_two,), mean, dtype=np.double)
    x[:N_over_two]+=delta
    x[N_over_two:]-=delta
    return np.random.permutation(x)

def array_samples(N_val):
    n_max = np.max(N_val)
    n_min = np.min(N_val)
    x = [np.full((k,), mean) for k in range(0, long)]
    
    for i in range(2, long):
        x[i] = np.full((2*i,), mean, dtype=np.double)
        x[i][:i]+=delta
        x[i][i:]-=delta
        x[i] = np.random.permutation(x[i])
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

def direct_first_var(x):
    """Первая оценка дисперсии через последовательное суммирование."""
    return direct_mean((x-direct_mean(x))**2)

