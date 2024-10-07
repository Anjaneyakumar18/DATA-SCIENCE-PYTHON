import numpy as np
# populating array from -10 to 9
arr=np.arange(-10,10)
print(arr)
#logical indexing with a single condition
print(arr[arr>0])
#logical indexing for even numbers
print(arr[arr%2==0])

#logical indexing for positive even numbers

print(arr[((arr%2==0) & (arr>0))])