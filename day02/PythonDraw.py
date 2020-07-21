import turtle
#from turtle import *
#import turtle as t
'''
    turtle库默认窗口中心为原点
    goto(x,y)
        从当前点画到(x,y)
    left(angle),right(angle)
        运行方向向左或向右旋转angle度
    colormode(mode)
        mode=1.0：使用RGB小数模式
        mode=255：使用RGB整数模式
    
'''
turtle.setup(650, 350, 200, 200)    #设置窗口长、宽与位置
turtle.Screen
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)                    #改变运行方向，参数为直角坐标系角度
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)                       #按照当前方向，直线前进40像素
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()