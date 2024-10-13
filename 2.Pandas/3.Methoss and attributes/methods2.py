import pandas as pd
data={
    "sno":[1,2,3,4,5,6,7,8,9,10],
    "name":["Anjaneya kumar","Anil kumar","teja","sai","Rakesh","Sri kanth","Tharun","Razak","Prasanth","Harsha"],
    "College":["NEC","NEC","NEC","HU","SMEC","SMD","KLU","NEC","TEC","NITP"]
}
labels=[2,3,4,5,1,6,7,8,9,10]
df=pd.DataFrame(data,index=labels)
print(df)
# sort_index method is used to sort the data frame bases on index values
print(df.sort_index())
# groupby method in pandas is same  as in sql groupn a set of rows based on a common attribute
grouped=df.groupby('College')
for college , name in grouped:
    print(f"{college} :")
    print(f'{list(name["name"])}')
