#109021049-羅浩維
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
# 畫出10個隨機圓
for _ in range(10):
    radius = np.random.rand() / 10  
    center = np.random.uniform(low=radius, high=1-radius, size=2)  
    circle = plt.Circle(center, radius, color='grey', alpha=radius*10) 
    ax.add_artist(circle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.show()
