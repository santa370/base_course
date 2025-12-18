import numpy as np
import matplotlib.pyplot as plt

def hyperbola(x_start, x_end, N):
   

    x = np.linspace(x_start, x_end, N)
    k = 1
    y = k / x
    
    plt.plot(x, y, label=f'y = {k}/x')
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')


hyperbola(0.1, 5, 100)

plt.savefig('DZ2.png')