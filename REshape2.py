import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr.reshape(3,3).base) #this is view
arr1=np.array([1,2,3,4,5,6,7,8])
arr2=arr1.reshape(2,2,-1) #same as arr1.reshape(2,2,2)
print(arr2)
print(arr2.shape)
arr3=np.array([[1,2,3],[4,5,6]])
arr4=arr3.reshape(-1)
print(arr4)
print(arr4.shape)