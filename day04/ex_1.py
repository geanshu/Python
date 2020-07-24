for i in range(1,10):
    for j in range(0,10):
        for p in range(0,10):
            for q in range(0,10):
                if i**4+j**4+p**4+q**4==1000*i+100*j+10*p+q:
                    print(str(i)+str(j)+str(p)+str(q))