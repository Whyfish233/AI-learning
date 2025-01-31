import numpy as np

A=np.arange(3,15).reshape((3,4))
print(A)
print(A.flatten())
for item in A.flat:
    print(item)
