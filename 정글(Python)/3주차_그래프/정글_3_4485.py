#녹색 옷 입은 애가 젤다지?
import sys
import heapq
import math

def sol(x,y):
    dr = [1,0,-1,0]
    dc = [0,-1,0,1]
    
    queue = []

    dist[x][y] = A[x][y]
    heapq.heappush(queue,[dist[0],x,y])

    while(queue):
        _, cur_x,cur_y = heapq.heappop(queue)
        if vis[cur_x][cur_y] == 1: continue
        vis[cur_x][cur_y] = 1
        for i in range(4):
            cr = cur_x + dr[i]
            cc = cur_y + dc[i]
            if cr < 0 or cr >= N or cc < 0 or cc >= N: continue
            dist[cr][cc] = min(dist[cr][cc],dist[cur_x][cur_y]+A[cr][cc])
            if not vis[cr][cc]:
                heapq.heappush(queue,[dist[cr][cc],cr,cc])
    print("Problem {}: {}".format(Now,dist[N-1][N-1]))

Now = 0
while(1): 
    Now +=1
    N = int(sys.stdin.readline())
    if N == 0:break
    A = []*N
    for i in range(N):
        A.append(list(map(int,sys.stdin.readline().split())))

    dist =[[math.inf for _ in range(N)] for _ in range(N)]
    vis =[[0 for _ in range(N)] for _ in range(N)]
    sol(0,0)


