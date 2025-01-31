import numpy as np
A=np.arange(14,2,-1).reshape((3,4))
print(A)
print(np.clip(A,5,9))
print(np.mean(A,axis=1))
