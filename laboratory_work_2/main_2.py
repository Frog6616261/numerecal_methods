import numpy as np
import matplotlib.pyplot as plt

import my_funcs as mf
import lab_funcs as lf
import lab_funcs_disp as lfd
import my_plot as mplt


# Solving sum

K = 7

print(np.sort([-5, -3, -4, -1, -2, 1,5,6,8]))

N = 1000
correct_sin_sum = mf.get_correct_sin_sum(N)
sin_perm_data = mf.get_sin_perm_samples(N)
sin_sort_data = mf.get_sin_sort_samples(N)
sin_abs_sort_data = mf.get_sin_abs_sort_samples(N)

sum_sin_perm = mf.Kahan_sum(sin_perm_data)
sum_sin_sort = mf.Kahan_sum(sin_sort_data)
sum_abs_sin_sort = mf.Kahan_sum(sin_abs_sort_data)

print("Relative sum error to Kahan permut sin data: ",
       lf.relative_error(correct_sin_sum, sum_sin_perm))
print("Relative sum error to Kahan sort sin data: ",
       lf.relative_error(correct_sin_sum, sum_sin_sort))
print("Relative sum error to Kahan abs sort sin data: ",
       lf.relative_error(correct_sin_sum, sum_abs_sin_sort))


x_permutated = lf.samples(K)
x_sort_up = np.sort(x_permutated)
x_sign_permutated = mf.get_any_sign_samples(K)
x_sign_sort = np.sort(x_sign_permutated)
x_sign_sort_abs = mf.get_any_sign_sort_samples(K)

permutated_sign_sum = mf.Kahan_sum(x_sign_permutated)
direct_sign_sum = mf.Kahan_sum(x_sign_sort)
direct_sign_sum_abs = mf.Kahan_sum(x_sign_sort_abs)

current_sign_sum = mf.exact_sign_sum()

print(mf.Kahan_sum(x_sort_up), mf.Kahan_sum(x_permutated))



print("суммирования для знаков:",
       permutated_sign_sum)
print("суммирования для знаков сортированных:",
       direct_sign_sum)
print("суммирования для знаков сортированных абсолютно:",
       direct_sign_sum_abs)


# 1
# при суммированиии постепенно , постепенно накапливается погрешность

# 2
# Алгоритм на каждом шаге учитывает поггрешность, после в конце ее выдает

# 3
# Да получим

# 4
# погрешность будет меняться, для абс погрешность сранима с машинной, для просто сорт плохая погрешность


# Solving dispersion and matsr

N = np.array([i for i in range(2, 1000)])
x = lfd.array_samples(N)
disp = lfd.exact_variance()

disp_one_sqrt_f = lfd.direct_first_var(x)
disp_one_sqrt_s = lfd.direct_second_var(x)
disp_two_sqrt = lfd.online_second_var(x)



mplt.plot_err_f_and_s(disp_one_sqrt_f, disp_one_sqrt_s, N)


# 5
# 

# 6
#
