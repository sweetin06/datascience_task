import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [np.nan, 2, np.nan], 'C': [4, 5, 7]}
df = pd.DataFrame(d)
print(df)

df1 = df.dropna()
print("Delete the row if the data frame have nan value:")
print(df1)

df2 = df.dropna(axis=1)
print("Delete the column if it have nan value")
print(df2)

df3 = df.fillna(10)
print("Fill the empty value")
print(df3)

df4 = df.interpolate()
print("Fill the empty value by interpolate , interpotale is mean of before and after element")
print(df4)

df5 = df.ffill()
print("Dataframe after forward fill:")
print(df5)

df6 = df.bfill()
print("Dataframe after backward fill:")
print(df6)
