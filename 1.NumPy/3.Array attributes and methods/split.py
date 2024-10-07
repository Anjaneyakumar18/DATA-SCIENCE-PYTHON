import numpy as np

arr=np.arange(10)
# split method in numpy divides the list into equal parts 
#if the split argument is not a factor of length of Array then throws an error
print(np.split(arr,5))
