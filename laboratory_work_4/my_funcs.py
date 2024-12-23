import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import math

class Poly_Horn():
    def __init__(self, pn):
        """
        Создает многочлен с коэффициентами pn:
            self(x) = sum_n pn[n] * x**n.
        Коэффициенты pn перечисляются в порядке возрастания степени одночлена.
        """
        self.pn = pn

    def __call__(self, x):
        """
        Вычисляет многочлен на векторе значений x.
        """
        count_numbs = len(self.pn)-1
        cur_val_pol = self.pn[count_numbs]*x + self.pn[count_numbs-1]
        for pn in range(2, len(self.pn)):
            cur_val_pol = cur_val_pol*x + self.pn[count_numbs-pn] # Учитываем очередной одночлен.
        return cur_val_pol
    
class Poly():
    def __init__(self, pn):
        self.pn = pn

    def __call__(self, x):
        a = 1. # Здесь мы накапливаем степени x**n.
        p = 0. # Сюда мы помещаем сумму одночленов.
        for pn in self.pn:
            p += a*pn # Учитываем очередной одночлен.
            a *= x # Повышаем степень одночлена
        return p


# Вспомогательная функция для счета матрицы Вандермонда.
def vandermonde(xn):
    return np.power(xn[:,None], np.arange(len(xn))[None,:])

# Напишем функцию, которая будет находить интерполяционных многочлен через решение системы.
def interp_naive(xn, fn):
    """
    Возвращает интерполяционный многочлен, принимающий в точках xp значение fp.
    """
    M = vandermonde(xn)
    # Мы используем функцию numpy для решения линейных систем.
    # Методы решения линейных систем обсуждаются в другой лабораторной работе.
    pn = np.linalg.solve(M, fn)
    return Poly(pn)

def interp_Horn(xn, fn):
    """
    Возвращает интерполяционный многочлен, принимающий в точках xp значение fp.
    """
    M = vandermonde(xn)
    # Мы используем функцию numpy для решения линейных систем.
    # Методы решения линейных систем обсуждаются в другой лабораторной работе.
    pn = np.linalg.solve(M, fn)
    return Poly_Horn(pn)

# Вычисление определителя
def det_theory(x):
  det = 1
  for j in range(len(x)):
    for i in range(j):
      det = det * (x[j] - x[i])
  return det


# Невязка
# Шаг 1: Создание матрицы Вандермонда
def vandermonde_matrix(x):
    return np.vander(x, increasing=True)

# Шаг 2: Число обусловленности
def condition_number(matrix):
    return np.linalg.cond(matrix)

# Шаг 3: Решение системы
def solve_system(V, b):
    c = np.linalg.solve(V, b)
    return c

# Шаг 4: Теоретическое предсказание погрешности
def theoretical_error(cond, delta_b, b_norm):
    return cond * (delta_b / b_norm)

def get_residual(x):
    # Генерация матрицы Вандермонда
    matrix = vandermonde_matrix(x)
    
    # Создаем вектор b длины len(x)
    b = np.random.rand(len(x))
    
    # Добавляем небольшой шум к b
    b_noisy = b + 1e-4 * np.random.randn(len(x))
    
    # Решаем систему для "зашумленной" правой части
    c_noisy = solve_system(matrix, b_noisy)
    
    # Вычисляем невязку
    residual = np.linalg.norm(matrix @ c_noisy - b_noisy)

    return residual



#Рекурсивгые алгоритмы
def Aitken_coeffs(xn, fn):
  if len(xn) == 1:
    return fn

  return (np.insert(Aitken_coeffs(xn[1:], fn[1:]), 0, 0) 
          - xn[0] *np.append(Aitken_coeffs(xn[1:], fn[1:]), 0) 
          - np.insert(Aitken_coeffs(xn[:-1], fn[:-1]), 0, 0) 
          +  xn[-1] *np.append(Aitken_coeffs(xn[:-1],  fn[:-1]), 0)) / (xn[-1] - xn[0])

def Aitken(xn, fn):
  return Poly(Aitken_coeffs(xn, fn))



