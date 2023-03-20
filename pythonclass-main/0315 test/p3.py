y = eval(input('請輸入年份：'))

if y%4 !=0:
    print('平年')
elif y%4 ==0 and y%100!=0:
    print('閏年')
elif y%400==0:
    print('閏年')
else:
    print('平年')
