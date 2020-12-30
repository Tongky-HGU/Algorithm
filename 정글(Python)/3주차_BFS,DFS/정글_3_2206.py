# 벽 부수고 이동하기
import sys, math
from collections import deque
N, M = map(int,sys.stdin.readline().split())
A=[]
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip())))

def bfs():
    vis=[[[0,0] for _ in range(M)] for _ in range(N)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    queue = deque()
    queue.append([0,0,0])
    vis[0][0][0]=1
    while(queue):
        cur_r,cur_c,wall = queue.popleft()
        if cur_r == N-1 and cur_c == M-1:
            # for i in range(N):
            #     print(vis[i])
            return vis[cur_r][cur_c][wall]
        for i in range(4):
            cr = cur_r +dr[i]
            cc = cur_c +dc[i]
            if cr < 0 or cr >= N or cc < 0 or cc >= M: continue
            if vis[cr][cc][wall]: continue
            if A[cr][cc] and wall == 0:
                vis[cr][cc][1] = vis[cur_r][cur_c][0]+1
                queue.append([cr,cc,1])
            if A[cr][cc] == 0:
                vis[cr][cc][wall] = vis[cur_r][cur_c][wall]+1
                queue.append([cr,cc,wall])
    return -1

def dihk

print(bfs())
