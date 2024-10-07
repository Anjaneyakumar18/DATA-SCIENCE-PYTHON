import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

print(f'Number of dimensions {arr.ndim}')
print(f'Shape of array is {arr.shape}')

print(arr.reshape((6,1)))
arr=arr.reshape((1,6))
print(f'The new shape is {arr.shape}')
print(arr)