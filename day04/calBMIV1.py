#a if bool else b <=> bool?a,b

height,weight=eval(input("请输入身高，体重:"))
bmi=weight /(height**2)
print("BMI={:.2f}".format(bmi))
who,nat='',''
if bmi<18:
    who,nat='偏瘦','偏瘦'
elif bmi<24:
    who,nat='正常','正常'
elif bmi<25:
    who,nat='正常','偏胖'
elif bmi<28:
    who,nat='偏胖','偏胖'
elif bmi<30:
    who,nat='偏胖','肥胖'
else:
    who,nat='肥胖','肥胖'
print('BMI标准为国标{},WHO标准{}'.format(nat,who))