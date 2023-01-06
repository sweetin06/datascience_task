import pandas as pd
df = pd.read_csv("C:\\Users\\Troniqs Rationale\\Downloads\\samplesheet1 - Sheet1.csv")
print("Data from csv:")
print(df)
print("______________________________")

df1 = df.set_index("team")
print("Data frame after set index")
print(df1)
print("________________________________")

df2 = df1.reset_index("team")
print("Data frame after reset index")
print(df2)
print("________________________________")

df3 = df.reset_index()
print("Reset of full dataframe")
print(df3)
print("________________________________")

