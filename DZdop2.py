import numpy as np
import matplotlib.pyplot as plt

def experement(p, e):
    phi = np.arange(0,8*np.pi, 0.01)
    a = 1 + e * np.cos(phi)
    r = p / a

    plt.plot(r)
    plt.savefig("experement.png")
experement(1, 0.1)
