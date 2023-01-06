import numpy as np
import pandas as pd

labels = ['a','b','c']
mydata = [10,32,22]
arr = np.array(mydata) #converting the array
dict = {'a':10,'b':20,'c':30}

series1 = pd.Series(data=mydata)
print("Create a series",series1)
print("______________________")

series2 = pd.Series(data=mydata,index=labels)
print("replace the index by its label",series2)
print("______________________")

series3 = pd.Series(arr)
print("Series in array",series3)
print("______________________")

series4 = pd.Series(dict)
print("Series of dictionary",series4)
print("______________________")

series5 = pd.Series([1,2,4,5],["hi","hlo","test","bye"])
print("Series of 2 list:",series5)

#operations
seriesadd = series1+series2
print(seriesadd)
