import numpy as np

mat1=np.matrix([[1,2],[3,4]])
mat2=np.matrix([[1,2],[3,4]])

print(f"Type is : {type(mat1)}")

print("matrix after adding mat1 and mat2")
print(np.add(mat1,mat2))

# addition operator
print(mat1+mat2)

