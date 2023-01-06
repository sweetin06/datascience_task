import numpy as np

array1 = np.arange(1,20,2)
print(array1)
arrtot = array1+array1
print("Total of two array")
print(arrtot)
arrsub = array1-array1
print("substraction of array:",arrsub)
arrmul = array1*array1
print("Multiplication of two array:",arrmul)
arrdev = array1/array1
print("Division of array:",arrdev)

arrcalc = array1*3
print("Operation value",arrcalc)

#positive square root
positivesquare = np.sqrt(arrtot)
print("Positive square roots:",positivesquare)

#exponent values
expovalues = np.exp(arrtot)
print("Exponential of all the elements in input array:",expovalues)

#log of array elements
logvalues = np.log(arrtot)