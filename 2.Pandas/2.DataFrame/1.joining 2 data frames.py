import pandas as pd

df1=pd.DataFrame({"col1":[i for i in range(10,101,10)],"col2":[i for i in range(10)]})
df2=pd.DataFrame({"col3":[i for i in range(100,1001,100)],"col4":[i for i in range(10)]})

newdf=df1.join(df2,on=df1["col2"]==df2["col3"])

print(newdf)