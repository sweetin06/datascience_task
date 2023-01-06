import numpy as np
import pandas as pd
from numpy.random import randn

value = np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print("Primary dataframe:")
print(df)
print("_______________________________")

df1 = df > 0
print("Check a dataframe value is true or false")
print(df1)
print("___________________")

df2 = df[df1]
print(df2)
print("__________________")

df3 = [df['X'] < 0]
print(df3)
print("___________________")

df4 = df[df['W']>1][['Y','Z']]
print(df4)
print("________________")

#df5 is about to write the code in different manner of df4
boolser = df['W']>1
result = df[boolser]
cols = ['Y','X']
df5 = result[cols]
print(df5)
print("_____________________")

#and operator is not suported with pandas , so here we are using &
df6 = df[(df['W']>1) & (df['Y'])>0]
print("Using a and operator")
print(df6)
print("__________________")

#or operator(|)
df7 = df[(df['W']>1) | (df['Y'])>0]
print("using a or operator")
print(df7)

#reset index - set the index
df8 = df.reset_index()
print("Dataframe after resets the index:")
print(df8)