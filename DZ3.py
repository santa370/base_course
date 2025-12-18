import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(start_angle, end_angle, N):
    
    h, k = 0, 0 
    a = 5       
    b = 3       
    
   
    t = np.linspace(start_angle, end_angle, N)
    
    
    x = h + a * np.cos(t)
    y = k + b * np.sin(t)
    
  
    plt.plot(x, y, color='blue')
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')

plot_ellipse(0, 2*np.pi, 100)


plt.savefig('DZ3.png')