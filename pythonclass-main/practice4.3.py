money = eval(input('賺多少錢(0-1000):'))

h= money//100
print('有',h,'個百元')
money = money-(h*100)
t = money//10
print('有',t,'個十元')
money= money-(t*10)
s = money//1
print('有',s,'個一元')
