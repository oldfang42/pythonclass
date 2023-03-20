m= eval(input('input first number: '))
n= eval(input('input second number: '))

if m>n:
    x = m
else:
    x = n
h = (m+1)*(n+1)
for i in range(x,h):
    if i % m ==0 and i % n ==0:
        print('lcm : ',i)
        break
