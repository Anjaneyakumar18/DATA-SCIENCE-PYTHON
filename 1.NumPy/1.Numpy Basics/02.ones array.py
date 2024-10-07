## creates a 2 dimentional m x n array with ones
'''
Syntax

np.ones((m,n),type=numpy.float64)
'''
import numpy as np

arr=np.ones((2,2))

print(arr)

#output
'''
[[1. 1.]
 [1. 1.]]
'''
print(type(arr[0][0]))

# output <class 'numpy.float64'>

# the default type of ones array is numpy.float64  we can modify it by passing argument


# Interger ones

print(np.ones((2,3),int))
'''
[[1 1 1]
 [1 1 1]]
'''
# string ones

print(np.ones((3,2),str))
'''
 ['1' '1']
 ['1' '1']]
'''

# complex numbers

print(np.ones((3,4),complex))

'''
[[1.+0.j 1.+0.j 1.+0.j 1.+0.j]
 [1.+0.j 1.+0.j 1.+0.j 1.+0.j]
 [1.+0.j 1.+0.j 1.+0.j 1.+0.j]]
'''