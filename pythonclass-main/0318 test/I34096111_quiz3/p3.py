n= eval(input('輸入正整數n: '))

for i in range(1,n+1):
    if i==1:
        print(" "*(n-i),"*"," "*(n-i))
    elif i%2==0:
        print(" "*(n-i),"* * "*(i//2)," "*(n-i-1))
    else:
        print(" "*(n-i),"* "*i," "*(n-i-1))
