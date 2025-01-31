import numpy as np

A=np.arange(12).reshape((3,4))
print(A)


print(np.vsplit(A,3))
print(np.hsplit(A,2))
