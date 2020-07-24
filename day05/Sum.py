def cmul(*a):
    sum=1
    for i in [*a]:
        sum*=i
    return sum

print(eval("cmul({})".format(input())))