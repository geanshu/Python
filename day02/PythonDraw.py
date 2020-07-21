import turtle
# from turtle import *
# import turtle as t
'''
    range(m,n)
        产生[m,n)的序列

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
turtle.penup()                      #画笔上升，离开窗口，不留下轨迹
turtle.fd(-250)
turtle.pendown()                    #画笔下落，落到窗口，留下轨迹
turtle.pensize(25)                  #画笔宽度
turtle.pencolor("purple")
# turtle.pencolor(0.63,0.13,0.94)
turtle.seth(-40)                    #setheading()，改变运行方向，参数为直角坐标系角度
for i in range(4):
    turtle.circle(40, 80)           #绘制弧形，参数为圆心，角度
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)                       #按照当前方向，直线前进40像素
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()                       #绘图完后不自动退出