#최단경로
import sys
from collections import deque
import heapq

V, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
A = [[] for _ in range(V+1)]

for _ in range(E):
    from_receive, to_recieve, d_recieve = map(int,sys.stdin.readline().split())
    A[from_receive].append([d_recieve,to_recieve])


vis = [0 for _ in range(V+1)]
dist = [-1 for _ in range(V+1)]

# print(A)
prior_queue=[]
heapq.heappush(prior_queue,[0,K])
dist[K] = 0
while prior_queue:
    d, cur = heapq.heappop(prior_queue)
    if vis[cur] == 1: continue
    vis[cur] = 1
    # print(cur)
    for i in range(0,len(A[cur])):
        d, to = A[cur][i]
        if dist[to] == -1:
            dist[to] = dist[cur]+d
        else:
            dist[to] = min(dist[to],dist[cur]+d)
        if not vis[to]:
            heapq.heappush(prior_queue,[dist[to],to])
    # print(dist)


# print(vis)
# print(dist)

for i in range(1,V+1):
    if dist[i] == -1:
        print("INF")
    else:
        print(dist[i])
    