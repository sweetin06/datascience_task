import pandas as pd
df = pd.read_csv("C:\\Users\\Troniqs Rationale\\Downloads\\samplesheet1 - Sheet1.csv")
print("Data from csv:")
print(df)
print("______________________________")

#create
df['Strike'] = ['100','300','450','120']
print("Create:")
print(df)
print("_________________________")

#insert
print("INSERT")
filled = df.ffill()
print(filled)
total = filled['score'].sum()
avg = filled['score'] / total
filled.insert(2, 'Average', avg)
print("After inserted")
print(filled)

#read
print("Read:")
print("Read the first 3 rows")
print(df[:3])
print("Read captain name and score")
selected = df.loc[[0,2],["captainname" ,"score"]]
print(selected)
print("select the row by it's index")
print(df.loc[1,"score"])

#update
print("Update:")
df.loc[0,"captainname"] = "bravo"
df["score"] = df["score"]*2
print("Update the fields:",df)

#Delete
print("Delete")
del1 = df.drop(3) #delete the row
del2 = del1.drop("score",axis=1)
print("After deletes one row and one column")
print(del2)
