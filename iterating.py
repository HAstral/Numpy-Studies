import numpy as np
#iterate 1D array
arr=np.array([1,2,3,4,5,6,7])
for x in arr:
    print(x)

#iterate 2D array
arr2=np.array([[1,2,3],[4,5,6]])
for x in arr2:
    print(x)

print('scalar version of 2D array:')
for x in arr2:
    for y in x:        
        print(y)
#iterate 3D array
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr3:
    print(x)

print('scalar version of 3D array:')
for x in arr3:
    for y in x:        
        for z in y:
            print(z)