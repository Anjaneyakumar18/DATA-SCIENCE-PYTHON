import numpy as np
lst1=[1,2,3]
lst2=[4,5,6]

arr=np.array([lst1,lst2])
print(arr)

'''
[[1 2 3]
 [4 5 6]]
 '''

# passing the 2 dimentional list as arguments

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
'''
[[1 2 3]
 [4 5 6]]
 '''
# passing one argument 2 dimentional list

lst4=[[1,2,3],[4,5,6]]

arr3=np.array(lst4)
print(arr3)
'''
[[1 2 3]
 [4 5 6]]
 '''
s=(1,2,3,4)
arrs=np.array(s)
print(arrs)

''' [1 2 3 4]'''

two_d_lst=[[1,0,3],[2,5,0]]

two_d_arr=np.array(two_d_lst,bool)

print(two_d_arr)
#Output 
'''
[[ True False  True]
 [ True  True False]]
'''

# As I said before Python typecastimg rules are to be followed