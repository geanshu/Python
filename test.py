import numpy as np
x=np.ones(shape=(32,1))
y=np.ones(shape=(32,))
z=x+y
print(z.shape)
print(z.sum())