# gruopby is grouped the data by any field

import numpy as np
import pandas as pd

datas = {'Company': ['KLC', 'YMC', 'KLC', 'YMC', 'DER', 'DER'],
         'Name': ['Jeev', 'Tom', 'Tim', 'Teen', 'Pop', 'Hill'],
         'Score': [200, 450, 231, 765, 340, 480]}
df = pd.DataFrame(datas)
print("Dataframe")
print(df)

comp = df.groupby('Company')
df2 = comp.mean()
print("Groupby Dataframe")
print(df2)

tot = df.groupby('Company')
df3 = tot.sum()
print("Total:")
print(df3)

counts = df.groupby('Company').count()
print("Counts data")
print(counts)

maxvalue = df.groupby('Company').max()
print("Maximum value:")
print(maxvalue)

minvalue = df.groupby('Company').min()
print("Minimum value:")
print(minvalue)

details = df.groupby('Company').describe()
print("Discribed")
print(details)
