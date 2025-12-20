import numpy as np
import matplotlib.pyplot as plt



def logarifmic_spir(b):
    phi = np.arange(0,8*np.pi, 0.01)
    r = np.exp(b * phi)

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.savefig("logarifmic_spir.png")

logarifmic_spir(0.3)
plt.close()

def arh_spir(k):
    phi = np.arange(0,8*np.pi, 0.01)
    r = k * phi

    x = r * np.cos(phi)
    y = r * np.sin(phi)
    plt.plot(x, y)
    plt.savefig("arh_spir.png")
arh_spir(1)
plt.close()

def wand_spir(k):
    phi = np.arange(0.01, 8*np.pi, 0.09)
    r = k / phi**0.5

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.axis("equal")
    plt.savefig("wand_spir.png")
    wand_spir(9)
    plt.close()


def roza_spir(k):
    phi = np.arange(0.01, 8*np.pi, 0.09)
    r = np.sin(k*phi)

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y)
    plt.savefig("roza_spir.png")

roza_spir(9)

