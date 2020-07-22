import time
'''
    time()
        获取时间戳，返回浮点数（从1970.1.1到当前时间的秒数）
    ctime()
        以人可读形式获取时间
    gmtime()
        返回一个时间类型对象，存储时间信息
    strftime(format,str)
        将时间对象格式化输出
        time.strftime("%Y-%m-%d %H:%M:%S",t)
            -%Y 年份 0000~9999，例如：1900
            -%m 月份 01~12，例如：10
            -%B 月份名称 January~December，例如：April
            -%b 月份名称缩写 Jan~Dec，例如：Apr
            -%d 日期 01~31，例如：25
            -%A 星期 Monday~Sunday，例如：Wednesday
            -%a 星期缩写 Mon~Sun，例如：Wed
            -%H 小时（24h制） 00~23，例如：12
            -%I 小时（12h制） 01~12，例如：7
            -%p 上/下午 AM,PM，例如：PM
            -%M 分钟 00~59，例如：26
            -%S 秒 00~59，例如：26
    strptime(str, tpl)
        将字符串转换为事件对象
        time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
        格式与上面的相同
    perf_counter()
        返回CPU级别的时间值，浮点型，需相减才能用
    sleep(time)
        程序暂停time秒   
'''
scale=10
print("------执行开始------")
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")