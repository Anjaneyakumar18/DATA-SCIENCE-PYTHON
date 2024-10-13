import pandas as pd
data={
    "sno":['a','b','c'],
    "Name":["AK","PK",'KK'],
    "Age":[20,23,22]
}

df=pd.DataFrame(data)
# single column indexing
print(df["sno"])

# multiple column indxeing

print(df[["sno","Name"]])