#109021049-羅浩維
import pandas as pd
import numpy as np
ser1 = pd.Series(list('abcde'))
ser2 = pd.Series(np.arange(5))
output = pd.concat([ser1, ser2], axis=1)
output.columns = ['col1', 'col2']
print(output)