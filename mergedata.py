import pandas as pd

# concating
data1 = {'name': ['dhoni', 'virat', 'gayle'],
         'key': ['k0', 'k1', 'k2'],
         'age': ['40', '33', '45'],
         'score': ['100', '87', '123']}

data2 = {'name': ['messi', 'ronaldo', 'neymar'],
         'key': ['k0', 'k1', 'k2'],
         'age': ['34', '33', '28'],
         'score': ['120', '134', '100']}

df1 = pd.DataFrame(data1, index=[0, 1, 2, ])
df2 = pd.DataFrame(data2, index=[4, 5, 6, ])
values = [df2, df1]

concatvalue = pd.concat(values)
print("CONCATED VALUES")
print(concatvalue)

concatvalue2 = df1.append(df2)
print("CONCATED VALUES BY APPEND")
print(concatvalue2)

# merging
mergedata = pd.merge(df1, df2, on=['key'])
print(mergedata)
