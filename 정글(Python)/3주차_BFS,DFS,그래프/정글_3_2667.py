# 단지 번호 붙이기
import sys
from collections import deque

N = int(sys.stdin.readline())

A=[]
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip())))

vis=[[0 for _ in range(N)] for _ in range(N)]

dr =[0,1,0,-1]
dc =[1,0,-1,0]

def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    vis[i][j]=1
    cnt = 0
    while(queue):
        cur = queue.popleft()
        cnt += 1
        for k in range(4):
            cr = cur[0] + dr[k]
            cc = cur[1] + dc[k]
            if cr < 0 or cr >= N or cc < 0 or cc >= N: continue
            if vis[cr][cc]: continue
            if A[cr][cc] == 0: continue
            queue.append([cr,cc])
            vis[cr][cc] = 1
    return cnt

building = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 1 and vis[i][j] == 0:
            building.append(bfs(i,j))

building.sort()

print(len(building))
for i in building:
    print(i)
