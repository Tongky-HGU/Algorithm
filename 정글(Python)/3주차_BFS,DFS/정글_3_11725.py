# 트리의 부모 찾기
import sys
from collections import deque

N = int(sys.stdin.readline())

A = [[] for i in range(N+1)]

for _ in range(N-1):
    a = list(map(int,sys.stdin.readline().split()))
    A[a[0]].append(a[1])
    A[a[1]].append(a[0])

vis=[0]*(N+1)
node=[0]*(N+1)

stack = deque()
stack.append(1)
while(1):
    i = stack.pop()
    vis[i] = 1
    for j in A[i]:
        if vis[j] == 1: continue
        node[j] = i
        vis[j] = 1
        stack.append(j)
    if len(stack) == 0:
        break

for i in range(2,N+1):
    print(node[i])


            