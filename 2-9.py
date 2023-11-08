#109021049-羅浩維
import numpy as np
import matplotlib.pyplot as plt
mu = 100
sigma = 10
data = np.random.normal(mu, sigma, 1000)
plt.hist(data, bins=30, density=True, alpha=0.5, color='b', edgecolor='black')
plt.title('Histogram of IQ')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.xticks(np.arange(40, 170, 20))
plt.yticks(np.arange(0, 0.035, 0.005))
plt.xlim([40, 160])
plt.ylim([0, 0.030])
plt.show()
