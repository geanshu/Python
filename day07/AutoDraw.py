'''
    map(func,para)
        对para中每个元素调用func函数
'''

import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600)
t.pencolor('red')
t.pensize(5)
#数据读取
datals=[]
f=open('day07/data.txt')
for line in f:
    line=line.replace('\n','')
    datals.append(list(map(eval,line.split(','))))
f.close()
#图形绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()