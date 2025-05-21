import numpy as np
arr=np.array([1,4,3,2,5,6,7,9,5,3,2,8,9,7,1])
x=np.where(arr==3)
print(x)
y=np.where(arr%2!=0) #odd values
print(y)