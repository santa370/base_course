import numpy as np
from scipy import constants as const

h = 100
ag = 45
bg = 35
g = 9.8

ar = np.deg2rad(ag)
br = np.deg2rad(bg)


n = g * h * np.tan(br)**2

d = 2 * np.cos(ar)**2 * (1 - np.tan(br) * np.tan(ar))

v = (n / d)**0.5

print(f"Значение v: {v}")


import numpy as np


from scipy.constants import k, hbar, pi, e

T = 200
e = 300

factor1 = 2 / np.sqrt(pi)
factor2 = (hbar * k * T)**(3/2)
factor3 = np.exp(e / (k * T))
N = factor1 * factor2 * factor3

print(f"Значение N: {N}")
