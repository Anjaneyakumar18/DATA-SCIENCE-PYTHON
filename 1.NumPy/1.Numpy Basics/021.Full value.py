# Fills the array of m x n order with a given value

'''
Syntax

np.full((m,n), value, dtype=type(value))
'''

import numpy as np

# Create a 2x3 array filled with the integer value 4
arr = np.full((2, 3), 4)
print(arr)
# Output:
# [[4 4 4]
#  [4 4 4]]

ar2=np.full((2,3),"AK")

print(ar2)

'''
[['AK' 'AK' 'AK']
 ['AK' 'AK' 'AK']]
'''

arr3=np.full((2,2),"AK",int)  # throws InvalidLiteralError