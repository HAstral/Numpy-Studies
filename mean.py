import numpy as np
from scipy import stats
arr=np.array([1,2,3,4,5,6,7,8,3,5,1,7,9])
print(np.mean(arr)) #for average value
arr=np.sort(arr)
print(arr)
print(np.median(arr)) #for median value
print(stats.mode(arr))
print(np.std(arr))