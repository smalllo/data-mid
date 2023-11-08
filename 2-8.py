#109021049-羅浩維
import pandas as pd
import numpy as np
data = np.random.randint(1, 100, 40).reshape(10, -1)
df = pd.DataFrame(data, columns=list('pqrs'), index=list('abcdefghij'))
def euclidean_distance(row1, row2):
    numeric_row1 = row1[['p', 'q', 'r', 's']]
    numeric_row2 = row2[['p', 'q', 'r', 's']]
    return np.linalg.norm(numeric_row1 - numeric_row2)
df['nearest_row'] = ""
df['dist'] = 0.0
for index, row in df.iterrows():
    min_dist = float('inf')
    nearest_row = None
    for index2, row2 in df.iterrows():
        if index != index2:
            distance = euclidean_distance(row, row2)
            if distance < min_dist:
                min_dist = distance
                nearest_row = index2
    df.at[index, 'nearest_row'] = nearest_row
    df.at[index, 'dist'] = min_dist
print(df)
