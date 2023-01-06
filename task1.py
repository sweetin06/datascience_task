import pandas as pd

#1.create the empty data frames
df = pd.DataFrame()
print("Empty data frame:",df)

#append a data in dataframe

df['city'] = ['Ngl','Chenai','Ctm']
df['state'] = ['TN','KL','MP']
df['country'] = ['India','Germany','China']
print("After appending a value in dataframe")
print(df)
print("_____________________________________")

#2.Import a xlsx file
file = pd.read_excel("C:\\Users\\Troniqs Rationale\\Downloads\\samplesheet.xlsx")
print("Data from excel:")
print(file)
print("_____________________________")

file1 = pd.read_csv("C:\\Users\\Troniqs Rationale\\Downloads\\samplesheet1 - Sheet1.csv")
print("Data from csv:")
print(file1)
print("______________________________")



#handle the NAN valus
#fillna function fill the nan values by the mentioned valus
handle1 = file1.fillna(2)
print("Using a fillna function")
print(handle1)
print("__________________")

#interpolate
handle2 = file1.interpolate()
print("Using interpolate")
print(handle2)
print("_____________________")

#backward fill
handle3 = file1.bfill()
print("Using a backwardfil:")
print(handle3)
print("__________________________________")

#forward fill
handle4 = file1.ffill()
print("Using a forwardfil:")
print(handle4)
print("___________________________")


