import time
for i in range(101):
    print("\r{:3}%".format(i),end='')   #end参数指字符串输出完后附加的字符，默认为\n
    time.sleep(0.1)