import numpy as np

def x_y (a, b, N):

    x = np.linspace(a, b, N)

    y = x**2

    return y


start = 0
stop = 4
points = 5

result_y = x_y(start, stop, points)

print(f"Значения X: {np.linspace(start, stop, points)}")
print(f"Значения Y: {result_y}")
