# 거의 최단 경로
import sys, math, heapq
from collections import deque

def dijkstra(a,array):
        vis =[0 for _ in range(N)]
        dist = [math.inf for _ in range(N)]
        queue = []
        dist[a] = 0
        heapq.heappush(queue,[dist[a],a])
        while(queue):
            _,cur = heapq.heappop(queue)
            if vis[cur]: continue
            vis[cur] = 1
            for d,to in array[cur]:
                if  dist[cur]+d < dist[to]:
                    dist[to] = dist[cur]+d
                if not vis[to]:
                    heapq.heappush(queue,[dist[to],to])
        return dist

# def dfs(a,d_in):
#     vis[a]=1
#     flag = False
#     if a == Y:
#         return True
#     for i in range(len(A[a])-1,-1,-1):
#         d_to,to = A[a][i]
#         if vis[to]: continue
#         if d_to + d_in > min_d: continue
#         result = dfs(to,d_in+d_to)
#         if result:
#             del A[a][i]
#             flag = True
#     if flag:
#         return True
#     else:
#         return False

def delete():
    queue = deque()
    queue.append(X)
    while(queue):
        cur = queue.popleft()
        for i in range(len(A[cur])-1,-1,-1):
            d_to,to = A[cur][i]
            if dist1[cur] + d_to == dist1[to] and dist1[to] + dist2[to] == min_d:
                queue.append(to)
                del A[cur][i]
            
while(1):
    N, M = map(int,sys.stdin.readline().split())
    if N == 0 and M == 0:break
    X, Y = map(int,sys.stdin.readline().split())
    A = [[]for _ in range(N)]
    B = [[]for _ in range(N)]

    for _ in range(M):
        x, y, d = map(int,sys.stdin.readline().split())
        A[x].append([d,y])
        B[y].append([d,x])

    dist1 = dijkstra(X,A)
    dist2 = dijkstra(Y,B)
    min_d = dist1[Y]

    delete()

    dist1 = dijkstra(X,A)
    if dist1[Y] == math.inf:
        print(-1)
    else:
        print(dist1[Y])
