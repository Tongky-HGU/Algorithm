#타임머신
import sys,math
N,M = map(int,sys.stdin.readline().split())
A = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,d = map(int,sys.stdin.readline().split())
    A[a].append([b,d])

# print(A)

vis = [math.inf for _ in range(N+1)]
vis[1] = 0

for _ in range(N-1):
    for i in range(N+1):
        for b,d in A[i]:
            if vis[b] > vis[i] + d:
                vis[b] = vis[i] + d

for i in range(N+1):
        for b,d in A[i]:
            if vis[b] > vis[i] + d:
                print(-1)
                exit()

for i in range(2,N+1):
    if vis[i] == math.inf:
        print(-1)
    else:
        print(vis[i])