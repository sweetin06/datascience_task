import pandas as pd

data = {'name': ['dhoni', 'virat', 'gayle', 'pope'],
        'key': ['k0', 'k1', 'k2', 'k3'],
        'age': [33, 56, 33, 45],
        'score': [100, 80, 135, 67]}

df = pd.DataFrame(data)
print(df)

dfunique = df['age'].unique()
print("Unique values:", dfunique)
dfuniquecount = df['age'].nunique()
print("Count of unique values:", dfuniquecount)
dfvaluecount = df['age'].value_counts()
print("Count of repated value: \n", dfvaluecount)

# conditional
df1 = df[df['age'] > 35]
print("Filtered value")
print(df1)

# boolean series
df2 = df['age'] > 35
print("Boolean filtered value")
print(df2)

# checking 2 condtions
df3 = df[(df['age'] > 35) & (df['score'] == 67)]
print("Checking 2 conditions")
print(df3)


# applying a custom function into the dataframe
def times(x):
    return x * 2


df4 = df['age'].apply(times)
print("Data after applying a customized value")
print(df4)

df5 = df['name'].apply(len)
print("Print the length of a mentioned age column:")
print(df5)

df6 = df['age'].apply(lambda x: x * 2)
print("Using lambda function")
print(df6)

df7 = df.drop('age', axis=1)
print("Delete the column")
print(df7)

df8 = df.sort_values('age')  # df.sort_values(by='age')
print("A sorted value")
print(df8)

df9 = df.isnull()
# check the null value, if there is a null value it return true otherwise it return false
print("Check the null values")
print(df9)

data1 = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar', ],
         'B': ['one', 'one', 'two', 'two', 'one', 'one', ],
         'C': ['x', 'y', 'x', 'y', 'x', 'y'],
         'D': [1, 3, 2, 5, 4, 1]}

dfdata1 = pd.DataFrame(data1)
print("Second dataframe:")
print(dfdata1)

df10 = dfdata1.pivot_table(values='D', index=['A', 'B'], columns=['C'])
print("Print a dataframe by using a PIVOT TABLES")
print(df10)


