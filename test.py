import numpy as np
import matplotlib.pyplot as plt
x=np.ones(shape=(32,1))
y=np.ones(shape=(32,))
z=x+y
print(z.shape)
print(z.sum())