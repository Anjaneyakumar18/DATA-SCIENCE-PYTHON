import numpy as np

arr=np.array([1,2,3,4,5,6,7])

if np.any(arr,where=arr>5):
    print("Yes there are numbers greater than 5")
else:
    print("There are no such numbers in arr which are greater than 5")

#we can even put large expressions

arr2=np.arange(10)

if np.any(arr,where=((arr%2==0) & (arr%3==0))):
    print("There are numbers which are factors of both 2 and 3")
else:
    print("No such numbers")


#Contains leap year or not

years1=np.array([2021,2022,2023])

years2=np.array([2000,2001,2004])


if np.any(years1,where=(years1 % 4 == 0) & (years1 % 100 != 0) | (years1 % 400 == 0)):
    print("Yes, contains a leap year")
else:
    print("No leap years")


if np.any(years2,where=(years2 % 4 == 0) & (years2 % 100 != 0) | (years2 % 400 == 0)):
    print("Yes, contains a leap year")
else:
    print("No leap years")
