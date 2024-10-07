# well we cannot append an element in to an preexisting array like python lists

# how its done in python lists

lst=[1,2,3,4]
lst.append(5)
#print(lst)  #[1,2,3,4,5]

# this type of appending is not possible in numpy arrays
# Every time you append you need a new array

'''
arr1:={1,2,3}
item_to_append:=4
arr2=np.append(arr1,item_to_append)
'''

import numpy as np

arr=np.arange(1,11)
print(arr)
item=11

after_appending=np.append(arr,item)

print(f"Before appending {arr}\nAfter appending {after_appending}")

# we can appending an array to an array also heer hopw it's done

appending_array=np.array([11,12,13,14,15])

final_array=np.append(arr,appending_array)

print(f"Array {appending_array} is appended to {arr}\nwhich resulted the array {final_array}")
