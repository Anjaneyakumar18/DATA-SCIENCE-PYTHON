import pandas as pd

labels=["Number","Name","Age"]
values=[545,"Anjaneya kumar",20]

data=pd.Series(values,index=labels)

print(data)