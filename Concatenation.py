import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.concatenate((a,b))) #concatenate means to join

c=np.array([[1,2,3],[4,5,6]])
d=np.array([[7,8,9],[10,11,12]])
print(np.concatenate((c,d),axis=1)) 