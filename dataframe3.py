import numpy as np
import pandas as pd
from numpy.random import randn

list1 = ['S1', 'S1', 'S2', 'S2']
list2 = [5, 6, 5, 6]
com_list = list(zip(list1, list2))
mul = pd.MultiIndex.from_tuples(com_list)

print("Combination of two lists")
print(com_list)

df = pd.DataFrame(randn(4, 2), mul, ['A', 'B'])
print(df)

df2 = df.loc['S1']
print("Print the data in S1")
print(df2)

df3 = df.loc['S1'].loc[6]
print("Print the S1 amd 6 :")
print(df3)

