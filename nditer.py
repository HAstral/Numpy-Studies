import numpy as np
#nditer is used for iterating over an array into scalar values
arr=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr):
    print(x)

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in np.nditer(arr3):
    print(x)

for x in np.nditer(arr[:,::2]): #with step 2
    print(x)