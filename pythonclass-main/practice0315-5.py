num = eval(input('input number:'))
h=0
e=0
z=0
nmi=0
nma=0
for i in range(1,2):
    print('no:',i)
    n = eval(input('='))
    nmi =n
    nma =n
    if n > 10:
        h=h+1
    elif n==10:
        e=e+1
    else:
        z=z+1
for i in range(2,num+1):
    print('no:',i)
    n = eval(input('='))
    if n > nma:
        nma =n
    if n < nmi:
        nmi =n
    if n > 10:
        h=h+1
    elif n==10:
        e=e+1
    else:
        z=z+1
print('max=',nma)
print('min=',nmi)
print(h,' num>10')
print(e,' num=10')
print(z,' num<10')
