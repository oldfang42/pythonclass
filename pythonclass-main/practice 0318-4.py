import random
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
a= random.randint(1,100)
b= random.randint(1,100)
print(a,b)
n= eval(input('要執行加法（0)還是減法（1)：'))
while n>1 or n<0:
    n= eval(input('要執行加法（0)還是減法（1)：'))
if n ==0:
    result = add(a,b)
elif n==1:
    result = sub(a,b)
print(result)
