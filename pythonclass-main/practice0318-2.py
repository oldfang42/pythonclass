while 1:
    c=0
    n= eval(input('請輸入用電度數: '))
    while n>950 or n<1:
        n= eval(input('請再次輸入用電度數: '))
    if n<=100:
        c=2.2*n
    elif n>100 and n<=300:
        c= 100*2.2+(n-100)*3.3
    else:
        c= 100*2.2+200*3.3+(n-300)*4.4
    print('應繳:','%.1f'%c,'元')
          
