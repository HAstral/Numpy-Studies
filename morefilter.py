import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
filter=[]
for i in arr:
    if i%2==0:
        filter.append(True)
    else:
        filter.append(False)
arr2=arr[filter]
print(arr2)