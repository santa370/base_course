import matplotlib.pyplot as plt
import numpy as np


def astroida_rotation(beta, R=3):
    alpha = np.arange(0, 2.5*np.pi, 0.1) 
    x = R * np.cos(alpha)**3
    y = R * np.sin(alpha)**3

    beta = np.deg2rad(beta)
    X = x * np.cos(beta) - y * np.sin(beta)
    Y = x * np.sin(beta) - y * np.cos(beta)
    return X,Y

plt.plot(x, y, ls='-', lw=3)
plt.xlim(-3, 3)
plt.xlim(-3, 3)
# plt.axis('equal')



plt.savefig('fig_1.png')