#스택 수열
import sys
from collections import deque
N = int(sys.stdin.readline())

a = deque()
x = [i for i in range(N,0,-1)]

ans = deque()

for i in range(N):
    a.append(int(sys.stdin.readline()))

print(a)
print(x)

for i in range(N):
    print(a)
    print(x)
    if a[-1] == x[-1]:
        deque.append(ans,"+")
        x.pop()
        deque.pop(a)
    else:
        trigger = False
        for j in range(1,len(x)):
            deque.append(ans,"+")
            if a[-1] == x[-j-1]:
                trigger = True
                for _ in range(j):
                    deque.append(ans,"-")
                # deque.append(ans,"+")
                deque.pop(a)
                x.pop(-j-1)
                break
        if trigger == False:
            break


print(ans)

        


                

