from random import random
from time import perf_counter
'''
random库
	seed(a=NONE)
		选择随机种子
		不给种子默认种子为第一次调用random时的系统时间
	random()
		产生随机数，0-1之间的小数
	randint(a,b)
		随机产生[a,b]间的整数
	randrange(m,n[,k])
		随机生成[m,n]间（以k为步长）的整数
	getrandbits(k)
		随机生成k比特长的整数
	uniform(a,b)
		随机生成(a,b)间的小数
	choice(seq)
		从序列seq中随机选择一项
	shuffle(seq)
		将seq序列随机打乱返回
'''

darts=10**6
hits=0
start=perf_counter()
for i in range(darts):
	x,y=random(),random()
	if x**2+y**2<1:
		hits+=1
pi=4*(hits/darts)
print("圆周率的值={:.5f}".format(pi))
print('计算时间为:{:.5f}s'.format(perf_counter()-start))
