import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = [0.1]
y = [0.1]
C = 0.3
D = 0.33

for _ in range(500):
    x.append (x[-1]**2 - y[-1]**2 + C)
    y.append (2 * x[-2] *  y[-1] + D)


fig, ax = plt.subplots
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
point, = ax.plot([], [], "red")

def update(i):
    point.set_data(x[:i], y[:i])
    return point,

ani = FuncAnimation(fig, update, frames=500, interval=20)
ani.save('points_animation.gif', writer='pillow', fps=20)
