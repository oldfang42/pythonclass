a = 0
sum= 0
f=0
f1=0
n = eval(input('請輸入正整數n: '))

while n>sum:
    a = a+1
    if a==1:
        f1=12
        sum=f1
    elif a==2:
        f2=35
        sum=f1+f2
        f = sum
        f1=f2
        f2=f 
    else:
        f=f1+f2
        sum=sum+f
        f1=f2
        f2=f

    
print('存到 ',n, '元需要 ',a,' 天')
