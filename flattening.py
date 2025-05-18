import numpy as np
a=np.array([[1,2,3],[2,3,4],[5,6,7]])
print(a)
print(a.flat[6]) #it gives seventh element cause index starts from 0
print(a.flatten()) #it gives a copy of the array in 1D