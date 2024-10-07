import numpy as np

mat1=np.matrix([[1,2],[3,4]])
mat2=np.matrix([[1,2],[3,4]])

# using numpy matmul method

print("Matrix after multiplication")
print(np.matmul(mat1,mat2))

# multiplication operator
print(mat1*mat2)