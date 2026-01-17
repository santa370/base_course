import numpy as np
import matplotlib.pyplot as plt

R = 1 
t = np.linspace(0, 2 * np.pi, 1000)
x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))



fig, ax= plt.subplots()
ball, = plt.plot(x, y, "-", color="r", label="ball")