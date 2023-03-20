n=eval(input('請輸入整數n:'))
print('質因數: ')
for i in range(1,n+1):
    for j in range(1,i+1):
        if n%i==0 and i!=j:
            if n%i==0 and i%j==0 and n!=i:
                
                print(i,end=' ')
