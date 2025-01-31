import numpy as np

A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
print(np.hstack((A,A,B)))

C=np.concatenate((A,B,B,A),axis=1)
print(C)



