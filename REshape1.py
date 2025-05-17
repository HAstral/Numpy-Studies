import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,1,2,3])
#1d to 2d
arr1=arr.reshape(3,4)
print(arr1)
#1d to 3d
arr2=arr.reshape(3,2,2)
print(arr2)