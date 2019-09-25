import math
N = int(input())
for i in range(N):
    num = int(input())
    c=0
    if num == 1:
        print('Not prime')
        continue
    for j in range(2,int(math.sqrt(num))+1):
        if num%j==0:
            c+=1
    if c>0:
        print('Not prime')
    else:
        print('Prime')
