a=int(input('enter the maths marks'))
b=int(input('enter the python marks'))
c=int(input('enter the problem solving techniques'))
d=int(input('enter the java marks'))
e=int(input('enter the marks'))
sum=a+b+c+d+e
value=sum/5
print(str(value)+"%")
if value>=90 and value<=100:
    print('grade is A')
elif value>=70 and value<=80:
    print('grade is B')
elif value>=50 and value<=60:
    print('grade is C')
elif value>=35 and value<=45:
    print('grade is D,justpass')
else:
    print('grade is FAIL')
