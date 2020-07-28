'''
文件打开    fo=open(路径,打开模式[,encoding=编码模式])
    打开模式可选参数：
        功能：
        'r'     只读模式，默认值，如果文件不存在，返回FileNotFoundError
        'w'     覆盖写模式，文件不存在则创建，存在则完全覆盖
        'x'     创建写模式，文件不存在则创建，存在则返回FileExistsError
        'a'     追加写模式，文件不存在则创建，存在则在文件最后追加内容
        '+'     与r/w/x/a一同使用，在原功能基础上增加同时读写功能
        打开模式
        'b'     二进制文件模式
        't'     文本文件模式，默认值
文件读取
    <f>.read(size=-1)
        读入全部内容，如果给出参数，读入前size长度
    <f>.readline(size=-1)
        读入一行内容，如果给出参数，读入该行前size长度
    <f>.readlines(hint=-1)
        读入文件所有行，以每行为元素形成列表,如果给出参数，读入前hint行
文件写入
    <f>.write(s)
        向文件写入一个字符串或字节流
    <f>.writelines(lines)
        将一个元素全为字符串的列表写入文件
    <f>.seek(offset)
        改变当前文件操作指针的位置
        offset含义如下：
            0 –文件开头；
            1 –当前位置；
            2 –文件结尾
文件关闭    fo.close()
'''

fo=open("day07/output.txt",'w+')
ls=['中国','美国','法国']
fo.writelines(ls)
fo.seek(0)  #关键行，如无该行写入完指针在文件尾，后无内容无法打印
for line in fo:
    print(line)
fo.close()