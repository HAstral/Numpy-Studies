import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
filter=arr>3
arr2=arr[filter]
print(filter)#this will print the boolean array
print(arr2)

filter1=arr%2==0
arr3=arr[filter1]
print(arr3)