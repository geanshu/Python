'''
    format()
        {<参数序号> ：<格式控制标记>}
        引导符号
            :
        填充
            用于填充的单个字符
        对齐
            < 左对齐
            > 右对齐
            ^ 居中对齐
        宽度
            槽设定的输出宽度，若长于槽宽度则按原宽度输出
        ,
            数字的千位分隔符
        .精度
            浮点数小数精度或字符串最大输出长度
        类型
            整数类型
                b, c, d, o, x, X
            浮点数类型
            e, E, f, %
'''

def Dayup(up):
    dayup=1
    for i in range(365):
        if i%7<2:
            dayup=dayup*(1-up)
        else:
            dayup*=(1+up)
    return dayup

up=0.01
dayup1=1.01**365
while Dayup(up)<dayup1:
    up+=0.001
print("工作日的努力值为：{:.3f}".format(up))