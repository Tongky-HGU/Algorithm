#쇠막대기
import sys
from collections import deque
A = str(sys.stdin.readline().rstrip())
stack = deque()
ans = 0
length = 0
for i in range(len(A)):
    if A[i]== '(':
        length+=1
    else:
        if stack[-1] == '(':
            length -=1
            ans += length
        else:
            ans +=1
            length -=1
    deque.append(stack,A[i])
print(ans)
    

        

