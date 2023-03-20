def p1(a, b):
    if b == 0:
        return None
    q = 0
    while a >= b:
        a = a-b
        q = q+1
    return q
a =eval(input('請輸入正整數a:'))
b =eval(input('請輸入正整數b:'))
print(p1(a,b))
