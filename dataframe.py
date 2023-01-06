import numpy as np
import pandas as pd
import random
from numpy.random import randn

value = np.random.seed(101)
df1 = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df1)
print("_______________________________")
print("Print only W field")
df2 = df1['W'] #print the W column
print("_______________________________")
print("Only W field",df2)
df3 = df1[['W','Z']]
print("W and Z",df3)
print("_______________________________")

#check the type of a variable
print("type of a variable:",type(df1))

#ADD One fields
df1['newfield'] = df1['W']+df1['Z']
print("Adding two fields:")
print(df1)
print("_______________________________")

#Drop one field
#axis = 0 is row and axis =1 is column
dfdelrow = df1.drop('newfield',axis=1)
print("Data frame after delete the col:")
print(dfdelrow)
print("_______________________________")

#delete the row, axis = 0
dfdelcol = df1.drop('D',axis=0)
print("Data frame after delete the row:")
print(dfdelcol)
print("_______________________________")

#selecting a rows
#there are two ways to locat the element
rowselect1 = df1.loc['C']
print("Selecting a row by itz label")
print(rowselect1)
print("_______________________________")

rowselect2 = df1.iloc[2]
print("Selecting a row by itz index value")
print(rowselect2)
print("_______________________________")

#select the cell
cellselect1 = df1.loc['B','Z']
print("Selects the particular cell:",cellselect1)


#selecting the subset of dataframe
subtable = df1.loc[['A','B'],['X','Y']]
print("Select the subset of a data")
print(subtable)

