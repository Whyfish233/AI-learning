import numpy as np
#a=np.array([[1,1],
#                   [0,1]])
#b=np.arange(4).reshape((2,2))

#c=a*b
#c_dot=np.dot(a,b)
#c_dot_2=a.dot(b)
#print(c)
#print(c_dot)
#print(c_dot_2) 

a=np.random.random((2,4))
print(a)
print(np.sum(a,axis=1))
print(np.min(a,axis=0))
print(np.max(a,axis=1))
