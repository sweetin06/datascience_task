import numpy as np
import random

#create an array of 10 zeros
zarray = np.zeros(10)
print("create an array of 10 zeros",zarray)

#create an array of 10 fives
farray = np.ones(10)*5
print("Create an array of 10 fives:",farray)

#Create an array of all the even integers from 10 to 50
onetofifty = np.arange(10,51)
print("Create an array of all the even integers from 10 to 50",onetofifty)

#Create a 3x3 matrix with values ranging from 0 to 8
matrix1 = np.arange(0,9)
print(matrix1)
matrix2 = matrix1.reshape(3,3)
print("3*3 array with 0 to 8",matrix2)
#eye 3*3
matrix3 = np.eye(3,3)
print("3*3 array with identical array",matrix3)
#random between 0 and 1
random1 = np.random.rand()
print("value between 0 and 1:",random1)
