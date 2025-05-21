import numpy as np
arrA=np.array([12,43,55,1])
arrB=[False,True,False,True]
arrC=arrA[arrB]
print(arrC) #returns the values of arrA where arrB is True
#filter using lambda function
x=[2,3,4,5,6,7,8,9]
y=list(filter(lambda x:x%2!=0,x))
print(y)
