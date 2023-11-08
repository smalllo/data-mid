#109021049-羅浩維
#可以使用for迴圈
import numpy as np
output = []
A = np.array([2,5,4,6,8,1,9])
for i in range(len(A)):
    if A[i] % 2 == 1:
        output.append(A[i])
output = np.array(output) 
print(output)
#可以使用numpy.where()
import numpy as np
A = np.array([2,5,4,6,8,1,9])
output = A[np.where(A % 2 != 0)]
print(output)
