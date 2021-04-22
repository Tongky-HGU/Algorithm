# 원 영역
# 재귀쓰려다가 망함^^
import sys
from collections import deque
N= int(sys.stdin.readline())
A=[]
for i in range(N):
    x, r = map(int,sys.stdin.readline().split())
    A.append([x-r,0])
    A.append([x+r,1])

A.sort(key=lambda x:(x[0],-x[1]))
# print(A)

cnt = 1

def solve(i):
    # print("new")
    global cnt
    stack= deque()
    inner = 0
    outer = 0
    while(1):
        # print(A[i])
        # print(stack)

        if A[i][1] == 0:
            stack.append([A[i][0],0])
        else:
            outer = abs(A[i][0] - stack[-1][0])
            if stack[-1][1] == outer:
                cnt+=2
                stack.pop()
                # print("cnt2")
            else:
                cnt+=1
                stack.pop()
                # print("cnt1")
            if len(stack) > 0:
                stack[-1][1] += outer
            else:
                return outer, i
        i += 1 

_ , ptr = solve(0)

while(1):
    if ptr == len(A)-1:
        break
    _ , ptr = solve(ptr+1)

print(cnt)