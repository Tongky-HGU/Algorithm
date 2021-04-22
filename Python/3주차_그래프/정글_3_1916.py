#최소비용구하기
import sys
import heapq
import math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
A = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, dist = map(int,sys.stdin.readline().split())
    A[a].append([dist,b])

S,K = map(int,sys.stdin.readline().split())

vis = [0 for _ in range(N+1)]
dist = [math.inf for _ in range(N+1)]

# print(A)

queue = []
heapq.heappush(queue,[0,S])
dist[S]=0
while(queue):
    _, cur = heapq.heappop(queue)
    if vis[cur] : continue
    # print(cur)
    vis[cur]= 1
    for d, to in A[cur]:
        dist[to] = min(dist[to],dist[cur]+d)
        if not vis[to]:
            heapq.heappush(queue,[dist[cur]+d,to])

# print(dist)
print(dist[K])

