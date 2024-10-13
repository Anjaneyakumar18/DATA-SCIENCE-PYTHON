import pandas as pd

data={
    "Nums":[i for i in range(1,11)]
}

df=pd.DataFrame(data)

print(df["Nums"].sum())