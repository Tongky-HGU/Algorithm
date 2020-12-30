# 네트워크 복구
import sys, heapq, math
N, M = map(int,sys.stdin.readline().split())
A =[[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int,sys.stdin.readline().split())
    A[a].append([d,b])
    A[b].append([d,a])

# print(A)

vis = [0 for _ in range(N+1)]
dist = [math.inf for _ in range(N+1)]
prev = [-1 for _ in range(N+1)]
queue = []
dist[1] = 0
heapq.heappush(queue,[dist[1],1])
while(queue):
    _, cur = heapq.heappop(queue)
    if vis[cur]: continue
    vis[cur]=1
    for d, to in A[cur]:
        if dist[cur] + d < dist[to]:
            prev[to] = cur
            dist[to]= dist[cur]+d
        if not vis[to]:
            heapq.heappush(queue,[dist[to],to])

print(N-1)
for i in range(2,N+1):
    print("{} {}".format(i,prev[i]))


