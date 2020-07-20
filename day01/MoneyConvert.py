str=input()
if str[0:3]=='RMB':
    num=eval(str[3:])/6.78
    print("USD{:.2f}".format(num))
elif str[0:3]=='USD':
    num=eval(str[3:])*6.78
    print("RMB{:.2f}".format(num))
else:
    print("输入格式错误")