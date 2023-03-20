p1 = ' '
p2 = ' '
p3 = ' '
p4 = ' '
p5 = ' '
p6 = ' '
p7 = ' '
p8 = ' '
p9 = ' '
p=0
start=1
while start==1:
    for i in range(1,3):
        if i==1:
            print("User one's turn to input now.")
            p =eval(input("Select input position 1~9："))
            while p>9 or p<1:
                print("User one's turn to input now.")
                p =eval(input("Select input position 1~9："))
            while (p1!=' 'and p==1)or (p2!=' 'and p==2)or (p3!=' 'and p==3)or (p4!=' 'and p==4)or (p5!=' 'and p==5)or (p6!=' 'and p==6)or (p7!=' 'and p==7) or (p8!=' ' and p==8)or (p9!=' ' and p==9):           
                print("User one's turn to input now.")
                p =eval(input("Select input position 1~9："))
            

            if p==1:
                p1 = 'O'
            elif p==2:
                p2 = 'O'
            elif p==3:
                p3 = 'O'
            elif p==4:
                p4 = 'O'
            elif p==5:
                p5 = 'O'
            elif p==6:
                p6 = 'O'
            elif p==7:
                p7 = 'O'
            elif p==8:
                p8 = 'O'
            elif p==9:
                p9 = 'O'
                
            print(p1,end='')
            print(p2,end='')
            print(p3)
            print(p4,end='')
            print(p5,end='')
            print(p6)
            print(p7,end='')
            print(p8,end='')
            print(p9)
            
            if (p1 == p2 == p3):
                if (p1=='O' and p2=='O'and p3=='O'):
                    print('user1 win')
                    start=0
                    break
                    
            elif(p1 == p5== p9):
                if (p1=='O' and p5=='O'and p9=='O'):
                    print('user1 win')
                    start=0
                    break

            elif(p1==p4==p7):
                if (p1=='O' and p4=='O'and p7=='O'):
                    print('user1 win')
                    start=0
                    break

            elif(p2==p5==p8):
                if (p2=='O' and p5=='O'and p8=='O'):
                    print('user1 win')
                    start=0
                    break
                    
            elif(p3==p6==p9):
                if (p3=='O' and p6=='O'and p9=='O'):
                    print('user1 win')
                    start=0
                    break
                    
            elif(p4==p5==p6):
                if (p4=='O' and p5=='O'and p6=='O'):
                    print('user1 win')
                    start=0
                    break
                    
            elif(p7==p8==p9):
                if (p7=='O' and p8=='O'and p9=='O'):
                    print('user1 win')
                    start=0
                    break

            elif(p3==p5==p7):
                if (p3=='O' and p5=='O'and p7=='O'):
                    print('user1 win')
                    start=0
                    break

            elif p1 !=' 'and p2!=' 'and p3!=' 'and p4!=' 'and p5!=' 'and p6!=' 'and p7!=' 'and p8!=' 'and p9!=' ':
                print('Tie')
                start=0
                break

            
        else:
            print("User two's turn to input now.")
            p =eval(input("Select input position 1~9："))
                 
            while p>9 or p<1:
                print("User two's turn to input now.")
                p =eval(input("Select input position 1~9："))
            while (p1!=' 'and p==1)or (p2!=' 'and p==2)or (p3!=' 'and p==3)or (p4!=' 'and p==4)or (p5!=' 'and p==5)or (p6!=' 'and p==6)or (p7!=' 'and p==7) or (p8!=' ' and p==8)or (p9!=' ' and p==9):           
                    print("User two's turn to input now.")
                    p =eval(input("Select input position 1~9："))
        
            if p==1:
                p1 = 'X'
            elif p==2:
                p2 = 'X'
            elif p==3:
                p3 = 'X'
            elif p==4:
                p4 = 'X'
            elif p==5:
                p5 = 'X'
            elif p==6:
                p6 = 'X'
            elif p==7:
                p7 = 'X'
            elif p==8:
                p8 = 'X'
            elif p==9:
                p9 = 'X'
            print(p1,end='')
            print(p2,end='')
            print(p3)
            print(p4,end='')
            print(p5,end='')
            print(p6)
            print(p7,end='')
            print(p8,end='')
            print(p9)
            if (p1 == p2 == p3):
                if (p1=='X' and p2=='X'and p3=='X'):
                    print('user2 win')
                    start=0
                    break
                    
            elif(p1 == p5== p9):
                if (p1=='X' and p5=='X'and p9=='X'):
                    print('user2 win')
                    start=0
                    break
                    
            elif(p1==p4==p7):
                if (p1=='X' and p4=='X'and p7=='X'):
                    print('user2 win')
                    start=0
                    break
                   
            elif(p2==p5==p8):
                if (p2=='X' and p5=='X'and p8=='X'):
                    print('user2 win')
                    start=0
                    break
                   
            elif(p3==p6==p9):
                if (p3=='X' and p6=='X'and p9=='X'):
                    print('user2 win')
                    start=0
                    break
                    
            elif(p4==p5==p6):
                if (p4=='X' and p5=='X'and p6=='X'):
                    print('user2 win')
                    start=0
                    break
                    
            elif(p7==p8==p9):
                if (p7=='X' and p8=='X'and p9=='X'):
                    print('user2 win')
                    start=0
                    break

            elif(p3==p5==p7):
                if (p3=='X' and p5=='X'and p7=='X'):
                    print('user2 win')
                    start=0
                    break

            elif p1 !=' 'and p2!=' 'and p3!=' 'and p4!=' 'and p5!=' 'and p6!=' 'and p7!=' 'and p8!=' 'and p9!=' ':
                print('Tie')
                start=0
                break
         
