import pandas as pd

from standered_deviation import s

data={
    "nums":[x for x in range(100)]
}

df=pd.DataFrame(data)

print(f" Vraiance as per prev {s**2}\nAs per cal {df.var()}")