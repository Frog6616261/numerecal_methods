import numpy as np
import matplotlib.pyplot as plt

import my_funcs as mf
import lab_funcs as lf
import lab_funcs_disp as lfd
import my_plot as mplt



x = lfd.samples(100000)
eps0 = np.finfo(np.double).eps
n = float(len(x))
mean = lfd.get_mean()
delta = lfd.get_delta()
variance = lfd.exact_variance()

theor_1 = 8*eps0*mean*delta**(0.5)
theor_2 = 4*eps0*mean**2

x_oneline_test=[1/2,4/7,3/5,11/19,5/19]
d1=lfd.oneline_first_var(x_oneline_test)
d2=lfd.online_second_var(x_oneline_test)
print('Сравнение однопроходных формул для первой и второй оценки дисперсии: разность получаемых значений',np.abs(d1-d2))

print("Размер выборки:", len(x))
print("Среднее значение:", lfd.exact_mean())
print("Оценка дисперсии:", lfd.exact_variance())
print("Ошибка среднего для встроенной функции:", lfd.relative_error(mean,np.mean(x)))
print("Ошибка дисперсии для встроенной функции:", lfd.relative_error(variance,np.var(x)))


print("Ошибка среднего для последовательного суммирования:", lfd.relative_error(mean,lfd.direct_mean(x)))

print("Ошибка второй оценки дисперсии для последовательного суммирования:",lfd.relative_error(variance,lfd.direct_second_var(x)))
print("Ошибка второй оценки дисперсии для однопроходного суммирования:",lfd.relative_error(variance,lfd.online_second_var(x)))


print("Ошибка первой оценки дисперсии для последовательного суммирования:",lfd.relative_error(variance,lfd.direct_first_var(x)))
print("Ошибка первой оценки дисперсии для однопроходного суммирования:",lfd.relative_error(variance,lfd.oneline_first_var(x)))


print("Теоретическая оценка ошибки дисперсии (по первой формуле):",theor_1)
print("Теоретическая оценка ошибки дисперсии (по второй формуле):",theor_2)

