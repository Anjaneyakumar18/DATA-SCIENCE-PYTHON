import numpy as np

lst=[1,2,3,4,5]

arr=np.array(lst)

print(type(arr),arr)


# you can also do like this as well

arr2=np.array([1,2,3])

print(arr2)

# we can even decide the datatype

print(np.array([1,2,3],complex))

'''
[1.+0.j 2.+0.j 3.+0.j]
'''

print(np.array([1,2,3],float))

'''
Same ython type casting rules are to be followed 
'''