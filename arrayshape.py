import numpy as np
arr0=np.array(3)
arr1=np.array([1,2,3])
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr0.shape) #O dimensional array
print(arr1.shape) #1 dimensional array with 3 elements
print(arr2.shape) #2 dimensional array with 2 rows and 3 columns
print(arr3.shape) #3 dimensional array with  2 "layers", each containing 2 rows and 3 columns
