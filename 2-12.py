#109021049-羅浩維
import pandas as pd
students_data = {'id': ['u001', 'u002', 'u003', 'u004', 'u005'],
                 'name': ['Alice', 'Bob', 'Cherry', 'David', 'Elle']}
students = pd.DataFrame(students_data)
scores_data = {'id': ['u001', 'u002', 'u005', 'u002', 'u004', 'u001', 'u002', 'u003', 'u004', 'u005'],
               'course': ['Data Science', 'Data Science', 'Data Science', 'Machine Learning', 'Machine Learning',
                          'AI', 'AI', 'AI', 'AI', 'AI'],
               'score': [68, 80, 70, 99, 56, 82, 78, 20, 92, 62]}
scores = pd.DataFrame(scores_data)
merged_df = pd.merge(students, scores, on='id')
passing_students = merged_df[(merged_df['course'] == 'AI') & (merged_df['score'] > 60)]
result = passing_students[['name', 'score']]
print(result)
