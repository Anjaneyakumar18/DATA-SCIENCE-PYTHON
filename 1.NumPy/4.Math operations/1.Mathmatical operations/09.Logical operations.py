## same as the arthematic operations logical operations can also be done as same
import numpy as np
arr1 = np.array([[True, False, True], [False, True, False]])
arr2 = np.array([[True, True, False], [False, False, True]])

logical_and = arr1 & arr2
print(logical_and)
# Output: [[ True False False]
#          [False False False]]



logical_or = arr1 | arr2
print(logical_or)
# Output: [[ True  True  True]
#          [False  True  True]]


logical_not = ~arr1
print(logical_not)
# Output: [[False  True False]
#          [ True False  True]]
