import numpy as np

# Creating two example arrays
arr1 = np.array([10, 20, 30])  # Binary: [1010, 10100, 11110]
arr2 = np.array([4, 5, 6])      # Binary: [100, 101, 110]

# Bitwise Operators
print("Bitwise Operators:")
bitwise_and = arr1 & arr2       # Bitwise AND
print(f"arr1 & arr2: {bitwise_and}")

bitwise_or = arr1 | arr2        # Bitwise OR
print(f"arr1 | arr2: {bitwise_or}")

bitwise_xor = arr1 ^ arr2       # Bitwise XOR
print(f"arr1 ^ arr2: {bitwise_xor}")

bitwise_not_arr1 = ~arr1        # Bitwise NOT on arr1
print(f"~arr1: {bitwise_not_arr1}")

# Left Shift
left_shift = arr1 << 1          # Left shift by 1
print(f"arr1 << 1: {left_shift}")

# Right Shift
right_shift = arr1 >> 1         # Right shift by 1
print(f"arr1 >> 1: {right_shift}")

# Relational Operators
print("\nRelational Operators:")
greater_than = arr1 > arr2
print(f"arr1 > arr2: {greater_than}")

less_than = arr1 < arr2
print(f"arr1 < arr2: {less_than}")

equal_to = arr1 == arr2
print(f"arr1 == arr2: {equal_to}")

not_equal_to = arr1 != arr2
print(f"arr1 != arr2: {not_equal_to}")

greater_than_or_equal = arr1 >= arr2
print(f"arr1 >= arr2: {greater_than_or_equal}")

less_than_or_equal = arr1 <= arr2
print(f"arr1 <= arr2: {less_than_or_equal}")

# Logical Operations
print("\nLogical Operations:")
arr3 = np.array([True, False, True])
arr4 = np.array([False, True, True])

logical_and = arr3 & arr4
print(f"arr3 & arr4: {logical_and}")

logical_or = arr3 | arr4
print(f"arr3 | arr4: {logical_or}")

logical_not = ~arr3
print(f"~arr3: {logical_not}")
