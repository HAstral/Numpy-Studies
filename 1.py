import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
arr4=np.array([[[[1,2,3],[1,3,2]],[[4,5,6],[7,8,9]]],[[[1,2,3],[1,3,2]],[[4,5,6],[7,8,9]]]])
print(arr4)

print(arr[0]*arr[3])
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2[0][1])
print(arr4.ndim)