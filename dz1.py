import numpy as np
import matplotlib.pyplot as plt

R = 1  # Радиус окружности
t = np.linspace(0, 4 * np.pi, 1000)

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

plt.figure(figsize=(10, 4))
plt.plot(x, y, color='blue')
plt.savefig('DZ1.png')