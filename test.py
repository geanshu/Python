import numpy as np
# x=np.ones(shape=(32,1))
# y=np.ones(shape=(32,))
# z=x+y
# print(z.shape)
# print(z.sum())

from scipy import optimize as op
c=np.array([1,1,1,10])
A_ub=np.array([[1,1,0,0],[0,0,1,1],[1,1,1,0]])
B_ub=np.array([2,2,3])
a=(0,1)
x1=(None,1)
x2=(None,1)
x3=(None,1)
x4=(None,1)
res=op.linprog(-c,A_ub,B_ub,bounds=(x1,x2,x3,x4))
print(res)
print('--------------------------------')
c=np.array([1,1,1,1])
A_ub=np.array([[1,1,0,0],[0,0,1,1],[1,1,1,0]])
B_ub=np.array([2,2,3])
x1=(None,1)
x2=(None,1)
x3=(None,1)
x4=(None,1)
res=op.linprog(-c,A_ub,B_ub,bounds=(x1,x2,x3,x4))
print(res)