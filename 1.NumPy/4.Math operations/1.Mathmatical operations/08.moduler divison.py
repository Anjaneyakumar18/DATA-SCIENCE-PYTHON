import numpy as np

#single number
arr1=np.array([1,2,3,4,5])
print(arr1%5)

# id array with 1 d array

arr2=np.array([5,4,3,2,1])
print(arr1%arr2)

# 2 d array with 2 d array

arr3=np.array([[1,2,3],[4,5,6]])
arr4=np.array([[1,2,3],[4,5,6]])

print(arr3%arr4)
