import numpy as np
from scipy import constants as const

h = 100
alpha_deg = 45
beta_deg = 35
g = const.g

alpha_rad = np.deg2rad(alpha_deg)
beta_rad = np.deg2rad(beta_deg)


numerator = g * h * np.tan(beta_rad)**2

denominator = 2 * np.cos(alpha_rad)**2 * (1 - np.tan(beta_rad) * np.tan(alpha_rad))

v = np.sqrt(numerator / denominator)

print(f"Значение v: {v}")


import numpy as np


from scipy.constants import k, hbar, pi, e

T = 200
epsilon = 300

factor1 = 2 / np.sqrt(pi)
factor2 = (hbar * k * T)**(3/2)
factor3 = np.exp(epsilon / (k * T))
N = factor1 * factor2 * factor3

print(f"Значение N: {N}")
