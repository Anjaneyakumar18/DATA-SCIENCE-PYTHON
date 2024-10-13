import pandas as pd

data={"Alphabet":[chr(65+i) for i in range(26)],"number":[i for i in range(1,27)]}

df=pd.DataFrame(data)

print(df)