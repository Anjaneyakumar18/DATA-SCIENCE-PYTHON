import pandas as pd
data={
    "sno":[1,2,3,4,5,6,7,8,9,10],
    "name":["Anjaneya kumar","Anil kumar","teja","sai","Rakesh","Sri kanth","Tharun","Razak","Prasanth","Harsha"],
    "College":["NEC","NEC","NEC","HU","SMEC","SMD","KLU","NEC","TEC","NITP"]
}
df=pd.DataFrame(data)

print(df)

# head methods returns top n record from df

print(df.head(5))

#tail method returns bottom n methods

print(df.tail(5))

# info method in pandas 

print(df.info())

# Give a over all view of dataframe
print(df.describe())

# sorts the dataframe according to the desired attribute
print(df.sort_values("name"))