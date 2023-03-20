f1= 10
f2= 25
f = 0
s = 0
a = eval(input('請輸入正整數a:'))
b = eval(input('請輸入正整數b:'))
if a ==1:
    s=f1
    print(a,' 天共存了 ',s,' 元')
elif a==2:
    s=f1+f2
    print(a,' 天共存了 ',s,' 元')
else:
    s=f1+f2
    for i in range(3,a+1):
        f = f1+f2
        s = s+f
        f1= f2
        f2= f

    print(a,' 天共存了 ',s,' 元')

f1= 10
f2= 25
f = 0
i = 1
s=0
while 1:
    if i==1:
        f=f1
        s=f
        if s>=b:
            print('存到',b,' 元需要 ',i,' 天')
            break
    elif i==2:
        f=f2
        s=f1+f
        if s>=b:
            print('存到',b,' 元需要 ',i,' 天')
            break
    else:
        f= f1+f2
        s=f+s
        f1 =f2
        f2 =f
        if s>=b:
            print('存到',b,' 元需要 ',i,' 天')
            break
    i= i+1
