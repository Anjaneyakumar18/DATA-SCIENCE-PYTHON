import pandas as pd

#importing the data frame from Attribute1.py  -- custom module 
from Attributes1 import df


# same as in numpy matrix and numpy array attribue T is used to get transpose 
print(df.T)

# empty attribute is used check weather the data frame is empty or not

print(df.empty)

#checking on empty data frame
new_df=pd.DataFrame()
print(new_df.empty)


# dtypes attribute in python is used to get data types of all attributes of a data frame
print(df.dtypes)

#  Same as in numpy pandas also has the data type preference 
new_df=pd.DataFrame([[1,"2"],["ak","pk"]])

print(new_df.dtypes)


# values attribute returns the list[list] which contains all dataframe data
print(df.values)

#shape attribute returns the shape of dataframe just like a matrix shape
print(df.shape)

#ndim return number dimenstions i.e always 2

print(df.ndim)

# size attribute returns the total no of cells in data frame 
# i.e rows*cols

print(df.size)

