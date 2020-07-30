#随机密码生成
import random

def genpwd(length):
    return random.randint(eval('1'+'0'*(length-1)),eval('9'*length))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
