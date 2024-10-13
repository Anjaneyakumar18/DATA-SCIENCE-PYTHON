import pandas as pd

data={
    "nums":[x for x in range(100)]
}

df=pd.DataFrame(data)

print(f"Corelation is {df.corr()}")