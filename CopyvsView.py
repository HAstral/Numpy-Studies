import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
y=arr.copy()
print(arr)
print(x)
print(y)
arr[0]=12
print(arr)
print(x) #the value of x[0] also changed
print(y) #the value of y[0] did not change
print(x.base) #this returns its base array
print(y.base) #this returns none