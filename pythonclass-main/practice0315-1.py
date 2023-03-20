num = eval(input('enter classmate num:'))
max=0
min=100
j=0
for i in range(1,num+1):
    print('第',i,'位同學',end ='')
    score = eval(input('grade:'))

    if score < min:
        min = score
    if score>max:
        max = score
    if score<60:
        j=j+1
print('minimum score=',min)
print('maximum socre=',max)
print('fail num=',j)
