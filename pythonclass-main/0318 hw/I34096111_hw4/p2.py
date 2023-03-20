import random
answer = random.randint(0,1000)
print('答案是：',answer)

while 1:
    guess = eval(input('猜一數字：'))
    if guess >answer:
        print('bigger')
    elif guess<answer:
        print('smaller')
    else:
        print('Bingo! 遊戲結束')
        break
