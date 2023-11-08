#109021049-羅浩維
import numpy as np
A = np.array([1,3,7,1,2,6,0,1])
output = np.where((A[1:-1] > A[:-2]) & (A[1:-1] > A[2:]))[0] + 1
print(output)
