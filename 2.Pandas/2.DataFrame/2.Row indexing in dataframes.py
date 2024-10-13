import pandas as pd

labels=["one","two","Three"]
df=pd.DataFrame({
    "ID":[1,2,3],
    "NAME":["AK","pk","kk"]
},index=labels)

## Using iloc 
print("using  iloc")
print(df.iloc[0])
print(df.iloc[1])

## using loc
print("using loc")
print(df.loc["one"])
print(df.loc["two"])
print(df.loc["Three"])

# conditional 
print("Conditional indexing")
print(df[df["ID"]==1])

#boolean indexing
print("Boolean indexing")
print(df[[False,True,False]])