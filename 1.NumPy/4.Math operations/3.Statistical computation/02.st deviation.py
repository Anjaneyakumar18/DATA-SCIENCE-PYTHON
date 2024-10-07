import numpy as np

arr=np.arange(10)

print(f"St dev for the inputed array is {arr.std()}")

# manually

arr2=np.arange(10)
s=0
for num in arr2:
    s+=num
mean=s/len(arr2)

st_sum=0
for num in arr2:
    st_sum+=(num-mean)**2
print(f"St dev is {(st_sum/len(arr2))**0.5}")