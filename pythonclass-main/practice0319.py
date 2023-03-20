def abc(x):
    if x==1:
        return 1
    else:
        return abc(x-1)*2+3

n = eval(input('第n個數字的數值:'))
print(abc(n))
