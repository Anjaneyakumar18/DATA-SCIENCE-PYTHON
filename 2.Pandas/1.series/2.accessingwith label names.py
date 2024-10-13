import pandas as pd

values=["Ak",545,"20Years old","CSE_A",'3edYear']
labels=["Name","Number","Age","Branch","Year"]

s=pd.Series(values,labels)

print(f' Name\t{s["Name"]}')


print(s[["Name","Number"]])