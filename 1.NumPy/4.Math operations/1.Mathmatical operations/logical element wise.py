import numpy as np

arr=np.array([True,True,False])

print(np.logical_and(arr,True))

new_arr=np.array([False,True,True])

print(np.logical_and(arr,new_arr))


'''
Likely logical_or() logical_xor()
'''

print(np.logical_or(arr,new_arr))
print(np.logical_xor(arr,new_arr))