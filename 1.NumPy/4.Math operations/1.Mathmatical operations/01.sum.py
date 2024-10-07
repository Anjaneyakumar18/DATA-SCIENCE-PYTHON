import numpy as np

arr=np.arange(1,11)

print(arr)

print(arr.sum())

# you can sumup all tyhe elements like this

s=0
for num in arr:
    s+=num
print(f"Sum of all the elements in the array {s}")