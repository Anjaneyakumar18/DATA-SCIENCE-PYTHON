import numpy as np

arr=np.arange(10)

print(f"The Variance of the aray is {np.var(arr)}")

# doing manually

arr2=np.arange(10)

s=0
for num in arr2:
    s+=num
mean=s/len(arr2)

var_sum=0
for num in arr2:
    var_sum+=(mean-num)**2
    
print(f"variance for the inputed array is {var_sum/len(arr2)}")