#109021049-羅浩維
import pandas as pd
data = {'col1': [5.0, 10.0, 20.0, 6.0, 77.0, 23.0, None],
        'col2': [1.0, 3.0, None, 5.0, 20.0, None, 40.0],
        'col3': [32, 8, 46, 5, 20, 37, 87],
        'col4': [None, None, 45.0, 20.0, None, 54.0, 72.0]}
df = pd.DataFrame(data)
missing_values = df.isnull().sum()
selected_columns = missing_values[missing_values <= 2].index
new_df = df[selected_columns]
print(new_df)
