for i in range(100,1000):
    h = i//100
    t = (i-h*100)//10
    s = (i-h*100-t*10)//1
    if h**3+t**3+s**3 ==i:
        print(i,end=' ')
