n= eval(input('請輸入正整數n: '))
S=0
for i in range(1,n+1):
    s=0
    for j in range(1,i+1):
        s=s+j
    S=S+s
print(S)
