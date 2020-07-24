def isprime(n):
    if n==1 or n==2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
sum=0
for i in range(2,100):
    if isprime(i):
        sum+=i
print(sum)