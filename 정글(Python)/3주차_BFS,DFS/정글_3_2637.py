#장난감 조립
import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
A = [[] for _ in range(N+1)]
order = [0 for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
for i in range(M):
    a = list(map(int,sys.stdin.readline().split()))
    A[a[0]].append([a[1],a[2]])
    order[a[1]] += 1
# print(A)
# print(order)

stack = deque()

while(1):
    flag = False
    for i in range(N,0,-1):
        if order[i] == 0:
            stack.append(i)
            order[i] = -1
            flag = True

    while(stack):
        cur = stack.pop()
        # print(cur)
        if len(A[cur]) > 0 :
            for i in range(len(A[cur])):
                order[A[cur][i][0]] -= 1
                ans[A[cur][i][0]] += (A[cur][i][1] * max(1,ans[cur]))
            ans[cur] = 0

    # print(order)
    # print(ans) 
    if flag == False: break

for i in range(1,N+1):
    if ans[i] >0:
        print(i,end=' ')
        print(ans[i])