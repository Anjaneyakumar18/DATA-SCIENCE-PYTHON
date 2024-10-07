import numpy as np

#subtracting relative elements in equal sized array

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print(arr1-arr2)

arr1=np.full((5,5),10)
arr2=np.full((5,5),3)

print(arr1-arr2)