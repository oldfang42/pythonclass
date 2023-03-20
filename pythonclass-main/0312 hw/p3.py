h= eval(input('input height: '))
age = eval(input('input age: '))

if h<=110:
    cost = 300
else:
    cost = 800

if age >=65:
    cost = cost*0.4
else:
    x= age % 10
    if x % 8 ==0:
        cost = cost*0.8
    else:
        cost = cost*1
print('cost: ',cost)
