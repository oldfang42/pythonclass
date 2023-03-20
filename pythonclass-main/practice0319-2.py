def money(x):
    if x==1:
        return 10
    else:
        return money(x-1)*2
def total(x):
    if x==1:
        return 10
    else:
        return total(x-1)+money(x)
print('第10天存入了:',money(10),'元')
print('10天共存了:',total(10),'元')
