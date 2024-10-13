import pandas as pd

data={
    "sno":[1,2,3],
    "name":["ak","pk","kk"],
    "age":[20,30,30]
    }

df=pd.DataFrame(data)

print(df)

df.loc[3]=[4,"rc",30]

print(df)
