import numpy as np



N = 3
M = 4


trigonometry_array = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = sin(N * i + N * j + 1)

for i in range(N):
    for j in range(M):
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0


print(trigonometry_array)
