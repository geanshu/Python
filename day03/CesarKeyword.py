origin=input()
after=''
small='abcdefghijklmnopqrstuvwxyz'
for i in range(len(origin)):
    k=origin[i]
    if k.lower() in small:
        k=small[(small.index(k.lower())+3)%26]
        if origin[i].isupper():
            k=k.upper()
    after+=k
print(after)