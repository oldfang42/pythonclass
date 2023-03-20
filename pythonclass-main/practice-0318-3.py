max = 0
fa = 0
i = 1
while i < 11:
    n = eval(input('請輸入第' + str(i) + '位同學成績：'))
    while n > 100 or n < 0:
        n = eval(input('請輸入第' + str(i) + '位同學成績：'))
    if n > max:
        max = n
    if n < 60:
        fa = fa + 1
    i = i + 1

print('Max: ', max)
print('不及格人數： ', fa)

max = 0
fa = 0
for i in range(1,11):
    n = eval(input('請輸入第' + str(i) + '位同學成績：'))
    while n > 100 or n < 0:
        n = eval(input('請輸入第' + str(i) + '位同學成績：'))
    if n > max:
        max = n
    if n < 60:
        fa = fa + 1


print('Max: ', max)
print('不及格人數： ', fa)
