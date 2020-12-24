# DFS와 BFS
import sys
from collections import deque

N, M, V = list(map(int,sys.stdin.readline().split()))

A=[]
for i in range(M):
    a=list(map(int,sys.stdin.readline().split()))
    A.append(a)
    A.append([a[1],a[0]])

A.sort(key=lambda x:(x[0],-x[1]))

#DFS
vis = [0]*(N+1)
stack = deque() #DFS

stack.append(V)
cnt = 0
while(1):
    cur = stack.pop()
    if vis[cur] == False:
        print(cur,end=' ')
        vis[cur] = True
        cnt+=1
        for i in range(2*M):
            if cur == A[i][0]:
                if vis[A[i][1]]== False:
                    stack.append(A[i][1])
    # if(cnt==N):
    if len(stack)==0:
        break
print('')

#BFS
A.sort(key=lambda x:(x[0],x[1]))

vis = [0]*(N+1)
queue = deque() #BFS

vis[V]=True
queue.append(V)
while(1):
    print(queue[0],end=' ')
    cur = queue.popleft()
    for i in range(2*M):
        if cur == A[i][0]:
            if vis[A[i][1]]== False:
                queue.append(A[i][1])
                vis[A[i][1]] = True
    if(len(queue)==0):
        break
print('\n')
