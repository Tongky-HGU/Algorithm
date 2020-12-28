# 줄 세우기
import sys
from collections import deque
sys.setrecursionlimit(100000)

N, M = map(int,sys.stdin.readline().split())

A = [[] for _ in range(N+1)]
order = [0 for _ in range(N+1)]
ans = []

for _ in range(M):
    a = list(map(int,sys.stdin.readline().split()))
    A[a[0]].append(a[1])
    order[a[1]] +=1

# print(A)
# print(order)
# print(vis)

def dfs(i):
    ans.append(i)
    order[i] = -1
    for j in range(len(A[i])):
        order[A[i][j]] -= 1
        if order[A[i][j]] == 0:
            dfs(A[i][j])
            
for i in range(1,N+1):
    if order[i] == 0:
        dfs(i)

print(*ans)

# print(order)
# print(vis)



    