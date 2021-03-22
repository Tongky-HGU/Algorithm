#바이러스
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

A = [[] for _ in range(N+1)]
vis = [0 for _ in range(N+1)]
ans = 0

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)

queue =[]
queue.append(1)
vis[1] =1

while(queue):
    cur = queue.pop()
    vis[cur] = 1
    ans += 1 
    for i in A[cur]:
        if vis[i]: continue
        vis[i] = 1
        queue.append(i)

print(ans-1)


