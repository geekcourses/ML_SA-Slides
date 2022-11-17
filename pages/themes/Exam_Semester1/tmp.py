import pandas as pd

# df = pd.DataFrame({
#   "name":['Maria', 'Petyr', 'Ivan'],
#   "age":[23, 21, 34],
#   "gender":['female', 'male', 'male']
# })


import os
cwd = os.getcwd()
print(cwd)

df = pd.read_csv('./users.csv')

r = df.gender.value_counts().loc['male']
print(r)