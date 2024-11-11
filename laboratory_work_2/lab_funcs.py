
import numpy as np
import matplotlib.pyplot as plt

base = 10

def exact_sum(K):
    """Точное значение суммы всех элементов."""
    return 1.

def samples(K):
    """"Элементы выборки"."""
    # создаем K частей из base^k одинаковых значений
    parts=[np.full((base**k,), float(base)**(-k)/K) for k in range(K, 0, -1)]
    # создаем выборку объединяя части
    samples=np.concatenate(parts)
    # перемешиваем элементы выборки и возвращаем
    return np.random.permutation(samples)

def sort_samples(K):
    """"Элементы выборки"."""
    # создаем K частей из base^k одинаковых значений
    parts=[np.full((base**k,), float(base)**(-k)/K) for k in range(K, 0, -1)]
    # создаем выборку объединяя части
    samples=np.concatenate(parts)
    # перемешиваем элементы выборки и возвращаем
    return samples

def direct_sum(x):
    """Последовательная сумма всех элементов вектора x"""
    s=0.
    for e in x:
        s+=e
    return s

def number_of_samples(K):
    """Число элементов в выборке"""
    return np.sum([base**k for k in range(0, K)])

def exact_mean(K):
    """Значение среднего арифметического по выборке с близкой к машинной точностью."""
    return 1./number_of_samples(K)

def exact_variance(K):
    """Значение оценки дисперсии с близкой к машинной точностью."""
    # разные значения элементов выборки
    values=np.asarray([float(base)**(-k)/K for k in range(0, K)], dtype=np.double)
    # сколько раз значение встречается в выборке
    count=np.asarray([base**k for k in range(0, K)])
    return np.sum(count*(values-exact_mean(K))**2)/number_of_samples(K)

def relative_error(x0, x):
    """Погрешность x при точном значении x0"""
    x0 = float(x0)
    x = float(x)
    return np.abs(x0 - x)/np.abs(x)

def Kahan_sum(x):
    s=0.0 # частичная сумма
    c=0.0 # сумма погрешностей
    for i in x:
        y=i-c      # первоначально y равно следующему элементу последовательности
        t=s+y      # сумма s может быть велика, поэтому младшие биты y будут потеряны
        c=(t-s)-y  # (t-s) отбрасывает старшие биты, вычитание y восстанавливает младшие биты
        s=t        # новое значение старших битов суммы
    return s


