p=0
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i**3+j**3+k**3==100*i+10*j+k:
                if p!=0:
                    print(',',end='')
                print(str(i)+str(j)+str(k),end='')
                p+=1