# in python list5 we haxe index() method to find the first occurence of the target element

# how we do in pytho lists

lst=[1,2,3,4,2]
print(lst.index(2)) # output : 1

# likely we have where() in numpy to find all the index of a target element
# returns the indices of target value in array as a NumPy array

import numpy as np 

arr=np.array([1,2,3,4,5,5,6,4,5,6,7,4])
indices=np.where(arr==4)
print(indices)