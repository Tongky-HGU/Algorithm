#최단경로
import sys,math,heapq
N, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
vis = [math.inf for _ in range(N+1)]
A = [[]for _ in range(N+1)]
for _ in range(E):
    a,b,d = map(int,sys.stdin.readline().split())
    A[a].append([b,d])
# print(A)
queue = []
heapq.heappush(queue,[0,K])
while(queue):
    # print(queue)
    dist,cur = heapq.heappop(queue)
    if vis[cur] != math.inf: continue
    vis[cur] = dist
    for b,d in A[cur]:
        if vis[b] != math.inf: continue
        heapq.heappush(queue,[dist+d,b]) 
# print(vis)

for i in range(1,N+1):
    if vis[i] == math.inf:
        print("INF")
    else:
        print(vis[i])

