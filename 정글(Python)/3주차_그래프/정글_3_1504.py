#특정한 최단경로
import sys
import heapq
import math

N, E = map(int,sys.stdin.readline().split())

A = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, dist = map(int,sys.stdin.readline().split())
    A[a].append([dist,b])
    A[b].append([dist,a])

v1,v2 = map(int,sys.stdin.readline().split())

def dijkstra(i):
    queue = []
    vis = [0 for _ in range(N+1)]
    dist = [math.inf for _ in range(N+1)]

    heapq.heappush(queue,[0,i])
    dist[i]=0

    while(queue):
        _, cur = heapq.heappop(queue)
        if vis[cur] : continue
        # print(cur)
        vis[cur]= 1
        for d, to in A[cur]:
            dist[to] = min(dist[to],dist[cur]+d)
            if not vis[to]:
                heapq.heappush(queue,[dist[cur]+d,to])
    return dist

first = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

ans1 = first[v1] + start_v1[v2] + start_v2[N]
ans2 = first[v2] + start_v2[v1] + start_v1[N]

if min(ans1,ans2) == math.inf:
    print(-1)
else:
    print(min(ans1,ans2))