import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Using the item() method to get a single element at a specific index (2 in this case)
# The item() method returns the Python scalar value at the given position
# In this example, it will return the element at index 2, which is '3'
ele = arr.item(2)

# Print the element
print(ele)  # Output will be 3
