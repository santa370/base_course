import numpy as np

x0 = 5
y0 = 7
v = 16
a = np.pi / 180*45
vx_0 = v * np.cos(a)
vy_0 = v * np.sin(a)
g = 9.8
coords = []

for t in np.arange(0, 5 ,0.1):
    x = x0 + vx_0 * t
    y = y0 + vy_0 * t - g * t**2 / 2

    coords.append([t, x, y])

coords = np.array(coords)
print(coords)
