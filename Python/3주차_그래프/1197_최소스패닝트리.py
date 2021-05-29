#최소신장 트리 프림
import sys,heapq

V,E = map(int,sys.stdin.readline().split())

A = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,d = map(int,sys.stdin.readline().split())
    A[a].append([d,b])
    A[b].append([d,a])

queue = []
vis = [[] for _ in range(V+1)]

vis[1] = 1
for d,b in A[1]:
    heapq.heappush(queue, [d,b])

ans = 0
cnt = 1
while(queue):
    # print(queue)
    dist,a = heapq.heappop(queue)

    if vis[a] == 1 : continue
    vis[a] = 1
    ans += dist
    cnt += 1
    for d,b in A[a]:
        heapq.heappush(queue, [d,b])
    if cnt == V:
        print(ans)
        break      