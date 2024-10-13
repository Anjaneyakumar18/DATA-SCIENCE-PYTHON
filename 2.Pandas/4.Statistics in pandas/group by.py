import pandas as pd

data={
    "name":["ak","ak","pk","pk"],
    "marks":[10,10,9,9]
}

df=pd.DataFrame(data)

print(df.groupby('name').sum('marks'))

print(df.groupby('name').mean('marks'))

