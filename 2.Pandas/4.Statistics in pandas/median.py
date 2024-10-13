import pandas as pd

data=[x for  x in range(1,12)]

df=pd.DataFrame(data)

print(df.median())