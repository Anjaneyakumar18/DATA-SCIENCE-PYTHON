import numpy as np
arr = np.array([[3, 1, 2], [5, 4, 6]])
sorted_arr = np.sort(arr, axis=1)  # Sort each row

print(sorted_arr)  # [[1, 2, 3], [4, 5, 6]]

new_arr=np.array([1,2,6,43,6,8,9])
print(np.sort(new_arr))

print(np.sort(arr))
#argsort()
# this methods return the sorted array indcxes of the array
print(np.argsort(new_arr))


