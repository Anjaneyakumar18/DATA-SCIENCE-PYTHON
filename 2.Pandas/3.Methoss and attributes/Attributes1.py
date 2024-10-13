import pandas as pd

data={
    "sno":(1,2,3),
    "name":("Ak","Pk","kk"),
    "age":(20,21,20)
}

labels=["I","II","III"]
df=pd.DataFrame(data,index=labels)

print(df)
 
#Find column headings 

print(df.columns)

#Index(['sno', 'name', 'age'], dtype='object') 

#Find Index headings 

print(df.index)

#Index(['I', 'II', 'III'], dtype='object')

