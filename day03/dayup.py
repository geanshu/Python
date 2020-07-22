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