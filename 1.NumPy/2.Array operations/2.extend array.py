# extendingb an array is not possible in NumPy like we do in python lists 

# How we do in Python Lists

lst1=[1,2,3]
lst2=[4,5,6]
lst1.extend(lst2)
#print(lst1)   ## [1,2,3,4,5,6]

# but we can use cancatination method for this

import numpy as np

arr1=np.arange(1,11)
arr2=np.arange(11,21)
concat_array=np.concatenate((arr1,arr2))

print(concat_array)

# this is very much similar to appending an array to an array

'''
______________________________________________________
|np.append()          |      np.concatenate()         |
|_____________________|________________________ ______|
|when you are         | when you have to append more  |
|dealing with only    |than one array to a prexisting |
|one array then use   |array the you better use       |
|np.append()          |np.concatenate()               |
-------------------------------------------------------

'''

a1=np.arange(1,11)
a2=np.arange(11,21)
a3=np.arange(21,31)

final_arr=np.concatenate([a1,a2,a3])

print(final_arr)