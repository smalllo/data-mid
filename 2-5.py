#109021049-羅浩維
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 100)
y_sqrt_x = np.sqrt(x)
y_x = x
y_x_squared = x**2
y_2_power_x = 2**x
plt.figure(figsize=(10, 6))
plt.plot(x, y_sqrt_x)
plt.plot(x, y_x)
plt.plot(x, y_x_squared)
plt.plot(x, y_2_power_x)
plt.show()
