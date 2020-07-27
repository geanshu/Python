'''
集合：用于数据去重
    -集合类型与数学中的集合概念一致
    -集合元素之间无序，每个元素唯一，不存在相同元素
    -集合用大括号{} 表示，元素间用逗号分隔
    -建立集合类型用{} 或set()，建立空集合类型，必须使用set()
    S|T     并，返回一个新集合，包括在集合S和T中的所有元素
    S-T     差，返回一个新集合，包括在集合S但不在T中的元素
    S&T     交，返回一个新集合，包括同时在集合S和T中的元素
    S^T     补，返回一个新集合，包括集合S和T中的非相同元素
    S<=T或S<T   返回True/False，判断S和T的子集关系
    S>=T或S>T   返回True/False，判断S和T的包含关系
    S|=T    并，更新集合S，包括在集合S和T中的所有元素
    S-=T    差，更新集合S，包括在集合S但不在T中的元素
    S&=T    交，更新集合S，包括同时在集合S和T中的元素
    S^=T    补，更新集合S，包括集合S和T中的非相同元素
    S.add(x)        如果x不在集合S中，将x增加到S
    S.discard(x)    移除S中元素x，如果x不在集合S中，不报错
    S.remove(x)     移除S中元素x，如果x不在集合S中，产生KeyError异常
    S.clear()       移除S中所有元素
    S.pop()         随机返回S的一个元素，更新S，若S为空产生KeyError异常
    S.copy()        返回集合S的一个副本
    len(S)          返回集合S的元素个数
    x in S          判断S中元素x，x在集合S中，返回True，否则返回False
    x not in S      判断S中元素x，x不在集合S中，返回True，否则返回False
    set(x)          将其他类型变量x转变为集合类型
序列包括：列表与元组
序列（元组也基本支持）
    x in s              如果x是序列s的元素，返回True，否则返回False
    x not in s          如果x是序列s的元素，返回False，否则返回True
    s+ t                连接两个序列s和t
    s*n 或n*s           将序列s复制n次
    s[i]                索引，返回s中的第i个元素，i是序列的序号
    s[i: j]或s[i: j: k] 切片，返回序列s中第i到j以k为步长的元素子序列
    len(s)              返回序列s的长度，即元素个数
    min(s)              返回序列s的最小元素，s中元素需要可比较
    max(s)              返回序列s的最大元素，s中元素需要可比较
    s.index(x) 或 s.index(x, i,j)：返回序列s从i开始到j位置中第一次出现元素x的位置
    s.count(x)          返回序列s中出现x的总次数
列表
    ls[i] = x           替换列表ls第i元素为x
    ls[i: j: k]= lt     用列表lt替换ls切片后所对应元素子列表
    del ls[i]           删除列表ls中第i元素
    del ls[i: j: k]     删除列表ls中第i到第j以k为步长的元素
    ls+= lt             更新列表ls，将列表lt元素增加到列表ls中
    ls*= n              更新列表ls，其元素重复n次
    ls.append(x)        在列表ls最后增加一个元素x
    ls.clear()          删除列表ls中所有元素
    ls.copy()           生成一个新列表，赋值ls中所有元素
    ls.insert(i,x)      在列表ls的第i位置增加元素x
    ls.pop(i)           将列表ls中第i位置元素取出并删除该元素
    ls.remove(x)        将列表ls中出现的第一个元素x删除
    ls.reverse()        将列表ls中的元素反转
字典：c++中的pair集合
    -采用大括号{}和dict()创建，键值对用冒号: 表示
    -{<键1>:<值1>, <键2>:<值2>, … , <键n>:<值n>}
    -<值> =<字典变量>[<键>]
    -<字典变量>[<键>] = <值>
    -[ ] 用来向字典变量中索引或增加元素
    deld[k]
        删除字典d中键k对应的数据值
    k in d
        判断键k是否在字典d中，如果在返回True，否则False
    d.keys()
        返回字典d中所有的键信息
    d.values()
        返回字典d中所有的值信息
    d.items()
        返回字典d中所有的键值对信息
    d.get(k, <default>)
        键k存在，则返回相应值，不在则返回<default>值
    d.pop(k, <default>)
        键k存在，则取出相应值，不在则返回<default>值
    d.popitem()
        随机从字典d中取出一个键值对，以元组形式返回
    d.clear()
        删除所有的键值对
    len(d)
        返回字典d中元素的个数
'''
def getNum():
    nums=[]
    iNumStr = input("请输入数字(回车退出)")
    while iNumStr!='':
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字(回车退出)")
    return nums

def mean(numbers):
    s=0.0
    for num in numbers:
        s+=num
    return s/len(numbers)

def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev+=(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med

n=getNum()
m=mean(n)
print("平均值:{},方差:{:.2},中位数:{}".format(m,dev(n,m),median(n)))