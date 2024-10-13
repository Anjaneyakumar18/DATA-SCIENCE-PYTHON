# import pandas
import pandas as pd

# creating label and values lists

label=["label1","label2","label3"]
values=["value1","value2","value3"]

#creating a series

s=pd.Series(values,label)
print(s)
#OutPut:::---
'''
label1    value1
label2    value2
label3    value3
'''
'''
| Attribute      | Description                                             |
|----------------|---------------------------------------------------------|
| .values        | Returns the underlying data as a numpy array.          |
| .index         | Returns the index (labels) of the Series.               |
| .dtype         | Returns the data type of the Series.                    |
| .size          | Returns the number of elements in the Series.           |
| .shape         | Returns the shape of the Series (number of elements,).  |
| .name          | Returns or sets the name of the Series.                 |
| .is_unique     | Checks if all elements in the Series are unique.        |
| .is_monotonic  | Checks if the Series is sorted (increasing or decreasing). |
| .empty         | Checks if the Series is empty (contains no elements).   |
| .nbytes        | Returns the number of bytes consumed by the Series. 
'''


print(s.values)#['value1' 'value2' 'value3']
print(s.index)#Index(['label1', 'label2', 'label3'], dtype='object')
print(s.dtype)#object
print(s.size)#3
print(s.shape)#(3,)
print(s.name)#None
print(s.is_unique)#True
print(s.is_monotonic_decreasing)#False
print(s.is_monotonic_increasing)#False
print(s.empty)#False
