import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import math

# Numpy уже имеет класс для полиномов: numpy.poly1d.
# Для полноты изложения мы реализуем свой класс.
class Poly():
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
