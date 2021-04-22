#알고스팟
import sys,math,heapq

C,R = map(int,sys.stdin.readline().split())

A = [[] for _ in range(R)]
for i in range(R):
    A[i] =list(map(int,sys.stdin.readline().rstrip()))

queue = []
dist=[[math.inf for _ in range(C)] for _ in range(R)]
vis=[[0 for _ in range(C)] for _ in range(R)]

dr= [1,0,-1,0]
dc= [0,-1,0,1]

heapq.heappush(queue,[0,0,0])
dist[0][0] = 0

while(queue):
    _,x,y =heapq.heappop(queue)
    if vis[x][y]: continue
    vis[x][y]=1
    for i in range(4):
        cr = x + dr[i]
        cc = y + dc[i]
        if cr < 0 or cr >= R or cc < 0 or cc >= C : continue
        dist[cr][cc] = min(dist[cr][cc],dist[x][y]+A[cr][cc])
        if vis[cr][cc] == 0:
            heapq.heappush(queue,[dist[cr][cc],cr,cc])

print(dist[R-1][C-1])