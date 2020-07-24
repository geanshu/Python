def prime(m):
    if m==1:
        return False
    if m==2:
        return True
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    return True

n = eval(input())
n=int(n)+1
sum=0
while sum<5:
    if prime(n):
        if sum!=0:
            print(',',end='')
        print(n,end='')
        sum+=1
    n+=1