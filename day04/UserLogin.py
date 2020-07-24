'''
    for:
        segment 1
    else:
        segment 2   没有遇见break时，运行segment 2
'''


for i in range(3):
    name=input()
    password=input()
    if name=='Kate' and password=='666666':
        print('登录成功！')
        break
else:
    print('3次用户名或者密码均有误！退出程序。')