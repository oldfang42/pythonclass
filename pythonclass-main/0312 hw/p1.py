n= eval(input('input the fibonacci sequence length: '))
fn1=1
fn2=1
if n==1:
    print(fn1)
elif n==2:
    print(fn1,end=' ')
    print(fn2)
else:
    print(fn1,end=' ')
    print(fn2,end=' ')
    for i in range(3,n+1,1):
        fn =fn1+fn2
        fn1=fn2
        fn2=fn
        print(fn,end=' ')

