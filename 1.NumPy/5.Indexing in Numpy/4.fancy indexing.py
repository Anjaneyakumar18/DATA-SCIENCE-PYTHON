import numpy as np

arr=np.arange(20,41)
index_array=np.array([1,3,5])
print(arr[index_array])

# method 2
#fetching even numbers from 0 to 99
arr2=np.arange(100)

print(arr2[np.arange(0,100,2)])