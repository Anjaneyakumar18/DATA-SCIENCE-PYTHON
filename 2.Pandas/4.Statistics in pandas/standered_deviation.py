import pandas as pd

data={
    "nums":[x for x in range(100)]
}

df=pd.DataFrame(data)

print(f'The data frame is {df}')
s=df.std()
print(f'St dev is {s}')