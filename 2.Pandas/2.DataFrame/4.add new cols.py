import pandas as pd

data={"col1":[x for x in range(1,6)],"col2":[x for x in range(10,51,10)]}

df=pd.DataFrame(data)

print(df)

df["col3"]=[x for x in range(100,501,100)]

print(df)

s={
    "col1":6,
    "col2":60,
    "col3":600
}

df.loc[5]=s
print(df)