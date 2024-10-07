import numpy as np
arr=np.arange(1,101)
print(f"The raw array is {arr}")
mean=arr.mean()
print(f'The mean for the array is {mean}')
#Custom mean calculation
arr=np.arange(101)
s=0
for i in range(len(arr)):
    s+=arr[i]
print(f"Sum is {s},There are {i} Observations hence mean is {s/i}")