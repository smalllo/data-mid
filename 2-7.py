#109021049-羅浩維
#Example	 1
#PPT當中的Original好像有問題
import numpy as np
A = np.array([1, 2, 3, 4, 5, 6])
print("Original:")
print(A)
shapes = [(3, 2), (2, 3), (6, 1)]
for shape in shapes:
    reshaped_array = A.reshape(shape)
    print(f"Reshape {shape[0]}x{shape[1]}:")
    print(reshaped_array)
#Example	 2
import numpy as np
A = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Original:")
print(A)
shapes = [(2, 4), (4, 2), (8, 1)]
for shape in shapes:
    reshaped_array = A.reshape(shape)
    print(f"Reshape {shape[0]}x{shape[1]}:")
    print(reshaped_array)
