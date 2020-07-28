def getNum():       #获取用户不定长度的输入
    return list(map(eval,(input()).split(',')))

def mean(numbers):  #计算平均值
    sum=0
    for num in numbers:
        sum+=num
    return sum/len(numbers)
    
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    numbers=sorted(numbers)
    if len(numbers)%2==1:
        return numbers[(len(numbers)-1)//2]
    else:
        return (numbers[(len(numbers)-1)//2]+numbers[(len(numbers)-1)//2+1])/2
    
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))
