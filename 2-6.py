#109021049-羅浩維
import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([10, 20, 30])
y1 = np.array([20, 40, 10])
x2 = np.array([10, 20, 30])
y2 = np.array([40, 10, 30])
fig, ax = plt.subplots()
ax.plot(x1, y1, label='line1-width-3', linewidth=3, color='blue')
ax.plot(x2, y2, label='line2-width-5', linewidth=5, color='red')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Two or more lines with different widths and colors with suitable legends')
ax.set_yticks(np.arange(10, 41, 5))
ax.set_xticks(np.arange(10, 31, 5))
ax.set_ylim(10, 40)
ax.set_xlim(10, 30)
ax.legend()
plt.show()
