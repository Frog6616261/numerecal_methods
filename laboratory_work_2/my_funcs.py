import numpy as np
import matplotlib.pyplot as plt

base = 10

def get_N_array(N_max):
    samples = np.concatenate([np.full(1, k) for k in range(1, N_max+1)])
    return samples

def get_correct_sin_sum(N):
    return (0.5)*(np.sin(N) - (np.tan(0.5))**(-1)*np.cos(N) + (np.tan(0.5))**(-1))

def get_sin_perm_samples(N):
    samples = np.concatenate([np.full(1, np.sin(k)) for k in range(1, N+1)])
    return np.random.permutation(samples)

def get_sin_sort_samples(N):
    return np.sort(np.concatenate([np.full(1, np.sin(k)) for k in range(1, N+1)]))

def get_sin_abs_sort_samples(N):
    data = np.sort(np.concatenate([np.full(1, np.sin(k)) for k in range(1, N+1)]))
    return data[np.argsort(np.abs(data))]

def Kahan_sum(x):
    s=0.0 # частичная сумма
    c=0.0 # сумма погрешностей
    for i in x:
        y=i-c      # первоначально y равно следующему элементу последовательности
        t=s+y      # сумма s может быть велика, поэтому младшие биты y будут потеряны
        c=(t-s)-y  # (t-s) отбрасывает старшие биты, вычитание y восстанавливает младшие биты
        s=t        # новое значение старших битов суммы
    return s

def array_reverse(x):
    long = len(x)
    y = np.full(long, 0)

    for i in range(0, long):
        y[(long-1) - i] = x[i]

    return y

def get_any_sign_samples(K):
    """"Элементы выборки"."""
    # создаем K частей из base^k одинаковых значений
    parts_pos=[np.full((base**k,), float(base)**(-k)/K) for k in range(0, K)]
    parts_neg=[np.full((base**k,), float(base)**(-k)/K * (-1)) for k in range(0, K)]
    # создаем выборку объединяя части
    samples_pos=np.concatenate(parts_pos)
    samples_neg = np.concatenate(parts_neg)
    samples = np.concatenate([samples_pos, samples_neg])
    # перемешиваем элементы выборки и возвращаем
    return np.random.permutation(samples)

def get_any_sign_sort_samples(K):
    """"Элементы выборки"."""
    # создаем K частей из base^k одинаковых значений
    parts_pos=[np.full((base**k,), float(base)**(-k)/K) for k in range(0, K)]
    parts_neg=[np.full((base**k,), float(base)**(-k)/K * (-1)) for k in range(0, K)]
    # создаем выборку объединяя части
    samples_pos=np.concatenate(parts_pos)
    samples_neg = np.concatenate(parts_neg)
    samples = np.sort(np.abs(np.concatenate([samples_pos, samples_neg])))
    long = len(samples)

    # восстанавливаем знаки
    for i in range(0, long):
        if i%2 == 0:
            samples[i] = samples[i]*(-1)

    # перемешиваем элементы выборки и возвращаем
    return samples

def exact_sign_sum():
    """Точное значение суммы всех элементов."""
    return 0.0
