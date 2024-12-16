
import numpy as np
import matplotlib.pyplot as plt
import lab_funcs as lf
import math
from scipy.optimize import fsolve

x = 0.5
k = 10e-9
N1 = np.linspace(0, 99, 100)
R = []

for i in range(0, len(N1)):
  b = x**(N1[i]+1)/((math.factorial(int(N1[i])))*(1+x)**(int(N1[i])))
  R.append(b)

for i in range(0, len(R)):
  if R[i] > k and k > np.finfo(np.double).eps:
    continue
  elif k > np.finfo(np.double).eps:
    print("Количество слагаемых, достаточное для получения значения логарифма с заданной точностью:",i)
    print("Максимальная погрешность остатка ряда равна", R[i])
    break
  else:
    print("Получить точность выше машинной невозможно")
    break