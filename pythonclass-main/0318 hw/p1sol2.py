def div_ab(a, b):
    if b == 0:
        return None
    q = 0
    while a >= b:
        k = 0
        while a >= (b << k):
            k = k+1
        k -= 1
        q += 1 << k
        a -= b << k
    return q
a = eval(input('請輸入正整數a:'))
b = eval(input('請輸入正整數b:'))
print(div_ab(a,b))
#首先，將b不斷地乘以2，直到得到的數大於等於a為止。假設這個數為c，並且在這個過程中，b被乘以了k次。也就是說，c >= a，且 c = b * (2^k)。

#然後，我們將c不斷地減去b，直到c小於b為止。這個過程中，我們減去了b的幾次方，其次方數字為k。最後得到的c就是a除以b的商數部分。

