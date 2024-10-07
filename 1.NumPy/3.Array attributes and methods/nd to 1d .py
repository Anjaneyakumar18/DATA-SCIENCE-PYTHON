import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

print(f"Number of dimensations are {arr.ndim}")
arr=arr.ravel()
print(f"New array :{arr}\nNew shape {arr.shape}")