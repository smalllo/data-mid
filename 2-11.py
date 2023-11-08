#109021049-羅浩維
import numpy as np
output_array = np.zeros((21, 34), dtype=int)
# 生成數列
sequence = [0, 1]
while sequence[-1] + sequence[-2] <= 21:
    sequence.append(sequence[-1] + sequence[-2])
output_array[15, 24:26] = sequence[2]
output_array[13:15, 24:26] = sequence[3]
output_array[13:16, 21:24] = sequence[4]
output_array[16:21, 21:26] = sequence[5]
output_array[13:21, 26:34] = sequence[6]
output_array[:13, 21:34] = sequence[7]
output_array[:, 0:21] = sequence[8]
for row in output_array:
    print(' '.join(f'{val:2}' for val in row))

