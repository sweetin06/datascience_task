import numpy as np
import random
from numpy.random import randint

list1 = [0,8,3]

list2 = [[5,4,2] , [9,44,23] , [32,43,2]]
#one dimentional
arr1 = np.array(list1)
print(arr1)

print("__________________")
#two dimentional
arr2 = np.array(list2)
print(arr2)
print("___________________")

#arraged the values
arrangded1 = np.arange(0,20)
print(arrangded1)
print("___________________")
#arrage the values by range
arrangded2 = np.arange(2,20,3)
print(arrangded2)
print("___________________")
#create the metric with 0, with a dimention
arrangded3 = np.zeros((4,5))
print("zero placed mrtrics:",arrangded3)
print("___________________")
#crete the metrics with 1, with a dimension
arranged4 = np.ones((3,5))
print(arranged4)
print("___________________")
#i line array
arranged5 = np.eye(5)
print(arranged5)
print("___________________")

#generating the random value in one dimentionals
random1 = np.random.rand(5)
print(random1)
print("___________________")
#generating the random value in multi dimentional
random2 = np.random.rand(6,3)
print(random2)
print("___________________")
#generating the random values
random3 = np.random.randn(4,4)
print(random3)
#generate the random integer
random4 = np.random.randint(2,3)
print(random4)
#generate the metric by reshape
random5 = arrangded1.reshape(4,5)
print(random5)
print("___________________")
#maximum value
maxvalue = random5.max()
print("Maximum Value:",maxvalue)
minvalue = random5.min()
print("Minimum Value:",minvalue)
print("__________________")
#location index
locationmax = random5.argmax()
print("Location of a max value:",locationmax)
print("___________________")
locationmin = random5.argmin()
print("Location of a min value:",locationmin)
print("____________________")
#datatype
typefind = random5.dtype
print("Type of array",typefind)
print("_____________________")
#randint
random6 = randint(2,10)
print(random6)


