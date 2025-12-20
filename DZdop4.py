import numpy as np
import matplotlib.pyplot as plt

def draw_ladder(num_steps):

    x_values = np.linspace(0, num_steps, num_steps * 100 + 1)
    
    y_values = np.floor(x_values)
    
    plt.step(x_values, y_values, where='post', color='blue')
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось (Значение N)')

draw_ladder(5)

plt.savefig('DZdop4.png')
plt.close()


import matplotlib.pyplot as plt

x = [1, 1, 2, 2, 3, 3, 4]
y = [1, 3, 3, 6, 6, 9, 9]

plt.plot(x, y, marker='o')

plt.savefig('DZdop4.1.png')





