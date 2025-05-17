import numpy as np
arr=np.array([[1,2,3],[3,4,5]])
print(np.transpose(arr)) #basically swap the axis

arr1=np.array([1,2,3,4,5,6,7,8])
arr2=arr1.reshape(4,2)
print(arr2)
print(arr2.T) #same as np.transpose(arr2)