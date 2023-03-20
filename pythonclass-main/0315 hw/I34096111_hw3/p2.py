S=1
for i in range(1,4):
    s=0
    for j in range(3,2*i+4,2):
        s = s+j
    S=S*s
print('S=',S)
