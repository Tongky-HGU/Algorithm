#등산
import sys, math, heapq
N, M, D, E = map(int,sys.stdin.readline().split())
H = [0]+(list(map(int,sys.stdin.readline().split())))
A = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, n = map(int,sys.stdin.readline().split())
    A[a].append([n,b])
    A[b].append([n,a])

# print(H)
# print(A)

def dij(i):
    vis = [0 for _ in range(N+1)]
    dist = [math.inf for _ in range(N+1)]
    queue = []
    dist[i] = 0
    heapq.heappush(queue,[dist[i],i])
    while(queue):
        _, cur = heapq.heappop(queue)
        if vis[cur]: continue
        vis[cur] = 1
        for d, to in A[cur]:
            if H[to] > H[cur]:
                dist[to] = min(dist[to],dist[cur]+d)
                if not vis[to]:
                    heapq.heappush(queue,[dist[to],to])
    return dist
            
uphill = dij(1)
downhill = dij(N)
# print(uphill)
# print(downhill)

ans= -math.inf
for i in range(1,N+1):
    s = H[i]*E - (uphill[i]+downhill[i])*D
    ans = max(ans,s)

if ans == -math.inf:
    print("Impossible")
else:
    print(ans)