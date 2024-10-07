# As we know, an array is a sequential (ordered) string of homogeneous data,
# which means all the elements in the array must be of the same data type.

import numpy as np

# Example with homogeneous data
lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print(arr)  # Output: [1 2 3 4 5]

# Example with heterogeneous data
lst2 = [1, 2, 3, "Ak", 3.4, 4 + 3j]
arr2 = np.array(lst2)
print(arr2)  # Output: ['1' '2' '3' 'Ak' '3.4' '(4+3j)']

# Example with mixed data types
lst3 = [1, 2, 3, 4.5]
arr3 = np.array(lst3)
print(arr3)  # Output: [1.  2.  3.  4.5]

# Knowledge point: In NumPy, when there are heterogeneous data types in
# an array, all the array elements are generalized to the same type.


lst4=[1,2,3,4+4j]

print(np.array(lst4))


#ORDER OF ARRAY DATATYPE ISSUE
'''
1.Complex number
2.Floating point number
3.Integer
4.String
'''