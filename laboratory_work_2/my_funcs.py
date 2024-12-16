import numpy as np
import matplotlib.pyplot as plt
import sys
import math as mt

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

######################################################### exp Task

def exp_evaluation(x, N=None):
  err = 1
  nk = 1
  acc = np.ones(N+1, dtype=float)
  acc[0] = x / (1-np.abs(x))
  for k in range(1, N+1):
    err = err * x
    acc[k] = err / np.abs(1 - np.abs(x) / k) / nk 
    for i in range (1, k+1):
      acc[k] = acc[k] / k
    nk = nk + 1
  return acc

def how_n_to_complete_exp(eps, x):
  eps0=np.finfo(np.double).eps
  N=1
  eps_now=N*(N+3)*x*eps0/2 + exp_evaluation(x, N)[-1]
  num=1
  hvost=exp_evaluation(x, num)[-1]
  summ_eps=num*(num+3)*x*eps0/2

  while hvost>=summ_eps:
    num=num+1
    hvost=exp_evaluation(x, num)[-1]
    summ_eps=num*(num+3)*x*eps0/2

  max_eps=summ_eps+hvost
  if eps>max_eps:
    while eps_now>=eps:
        N=N+1
        eps_now=N*(N+3)*x*eps0/2 + exp_evaluation(x, N)[-1]
    return N
  else:
     return 'Pososi, Epsilone is small'
  
def find_N(x, max_N = 1000):
    eps0=np.finfo(np.double).eps
    min_delta = sys.float_info.max
    result_N = 1

    for N in range(1, max_N):
        err_sum = (N * (N + 3) * x * eps0) / 2
        err_series = (np.pow(x, N + 1)) / (mt.factorial(N)*(N - x))
        cur_delta = np.abs(err_sum - err_series)
        if cur_delta <= min_delta:
           min_delta = cur_delta
           result_N = N
    
    return result_N
