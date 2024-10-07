#In python list you can easily pop elements using pop()
#How it's done in python lists
lst=[1,2,3,4,5]
lst.pop()
lst.pop(0)
# print(lst)  output: [2,3,4]

# But we donot have pop() in numpy array but we have np.delete()
import numpy as np
arr1=np.arange(1,11)
final=np.delete(arr1,1)
print(final)

# fining index first use where method
# np.where return te array of index of occurences
arr1=np.array([1,2,3,4,5,5,5,6,6,7,6,45,5,5])
index=np.where(arr1==5)
print(f"Element 5 is at {index}")

final=np.delete(arr1,index)
print(final)