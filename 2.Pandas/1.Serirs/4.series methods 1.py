import pandas as pd

# Creating a Series
index = [i for i in range(1, 13)]
values = [i for i in range(10, 101, 10)] + [pd.NA, pd.NA]
s = pd.Series(values, index)

# Displaying the Series
print("Original Series:")
print(s)

# Displaying the first 5 elements
print("\nFirst 5 elements of the Series:")
print(s.head(5))  # Returns the first 5 elements

# Displaying the last 5 elements
print("\nLast 5 elements of the Series:")
print(s.tail(5))  # Returns the last 5 elements

# Getting unique values from the Series
print("\nUnique values in the Series:")
print(s.unique())  # Returns unique values as a NumPy array

# Dropping duplicate values
print("\nSeries after dropping duplicates:")
print(s.drop_duplicates())  # Returns a Series with duplicates removed

# Descriptive statistics
print("\nDescriptive statistics of the Series:")
print(s.describe())  # Generates descriptive statistics

# Value counts
print("\nCounts of unique values in the Series:")
print(s.value_counts())  # Returns counts of unique values

# Sorting values
print("\nSeries sorted by values:")
print(s.sort_values())  # Returns a Series sorted by values

# Sorting by index
print("\nSeries sorted by index:")
print(s.sort_index())  # Returns a Series sorted by index

# Checking for null values
print("\nNull values in the Series:")
print(s.isnull())  # Returns a boolean Series indicating if values are null

# Checking for non-null values
print("\nNon-null values in the Series:")
print(s.notnull())  # Returns a boolean Series indicating if values are not null

# Casting the Series to a different data type
print("\nSeries after casting to string:")
print(s.astype(str))  # Casts Series to string data type

# Applying a function to the Series
print("\nSeries after applying a function (multiply by 2):")
print(s.apply(lambda x: x * 2 if pd.notnull(x) else x))  # Applies a function to each element

# Cumulative maximum
print("\nCumulative maximum of the Series:")
print(s.cummax())  # Returns the cumulative maximum

# Cumulative minimum
print("\nCumulative minimum of the Series:")
print(s.cummin())  # Returns the cumulative minimum

# Cumulative sum
print("\nCumulative sum of the Series:")
print(s.cumsum())  # Returns the cumulative sum

# Shifting the Series
print("\nSeries after shifting by 2 periods:")
print(s.shift(2))  # Shifts values by 2 periods

# Filling NA values
print("\nSeries after filling NA values with 0:")
print(s.fillna(0))  # Fills NA/NaN values with 0

# Dropping NA values
print("\nSeries after dropping NA values:")
print(s.dropna())  # Returns a Series with NA/null values removed

# Sampling random elements from the Series
print("\nRandom sample of 5 elements from the Series:")
print(s.sample(5))  # Returns a random sample of 5 items

# Checking for equality with another Series
s2 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, pd.NA, pd.NA], index)
print("\nAre the two Series equal?")
print(s.equals(s2))  # Checks if two Series are equal
