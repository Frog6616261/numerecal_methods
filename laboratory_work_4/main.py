import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import math
import lab_funcs as lf
import my_funcs as mf



N = 8 
x = np.logspace(-6,0,N) 
f = lf.Poly(np.random.randn(N))
y = f(x) 

P_Ait = mf.Aitken(x,y)
z = P_Ait(x)

print("Absolute error of values", np.linalg.norm(z-y))
print("Absolute error of coefficients", np.linalg.norm(f.pn-P_Ait.pn))

