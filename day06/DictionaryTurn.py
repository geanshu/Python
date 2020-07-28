dic=eval(input())
try:
    print({value:key for (key, value) in dic.items()})
except:
    print('输入错误')