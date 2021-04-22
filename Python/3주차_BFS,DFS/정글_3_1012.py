#유기농 배추
import sys
from collections import deque
def bfs(i,j):  
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    queue = deque()
    queue.append([i,j])
    vis[i][j] = 1
    while(queue):
        cur = queue.popleft()
        for i in range(4):
            cx = cur[1] + dx[i]
            cy = cur[0] + dy[i]
            if cx <0 or cx >= M or cy < 0 or cy >= N: continue
            if A[cy][cx] == 0: continue
            if vis[cy][cx] == 1: continue
            vis[cy][cx] = 1
            queue.append([cy,cx])

N = int(sys.stdin.readline())
for _ in range(N):
    M, N, K = map(int,sys.stdin.readline().split())
    A = [[0 for _ in range(M)] for _ in range(N)]
    vis = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        A[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not vis[i][j] and A[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
        
    