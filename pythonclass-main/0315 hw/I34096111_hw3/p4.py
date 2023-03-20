n = int(input("請輸入正整數n: "))

# 繪製菱形
for i in range(1, n+1):
    if i ==1:
        print(" "*(n-i), "*", " "*(n-i))
    elif i==2:
        print(" "*(n-i),"***"," "*(n-i))
    elif i==3:
        print(" "*(n-i),"* * *"," "*(n-i))
    elif i>2:
        print(" "*(n-i),"*"," "*(i-4),"*"," "*(i-4),"*"," "*(n-i))

for i in range(1,2*n+2):
    print("*",end='')
    if i==2*n+1:
        print('')
for i in range(n,0,-1):
    if i>3:
        print(" "*(n-i),"*"," "*(i-4),"*"," "*(i-4),"*"," "*(n-i))
    elif i==3:
        print(" "*(n-i),"* * *"," "*(n-i))
    elif i==2:
        print(" "*(n-i),"***"," "*(n-i))
    elif i ==1:
        print(" "*(n-i), "*", " "*(n-i))
