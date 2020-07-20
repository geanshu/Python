x=eval(input())
str="Hello World"
if x>0:
    i=0
    while i<len(str):
        if i+1<len(str):
            print(str[i]+str[i+1])
        else:
            print(str[i])
        i=i+2
elif x==0:
    print("Hello World")
else:
    for i in range(len(str)):
        print(str[i])