#전쟁전투
import sys
C, R = map(int,sys.stdin.readline().split())
A = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(R)]
vis = [[0 for _ in range(C)] for _ in range(R)]

W = 0
B = 0

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(i,j,team):
    global W,B
    queue =[[i,j]]
    cnt = 0
    while(queue):
        x, y = queue.pop()
        vis[x][y] =1
        cnt+=1
        for a in range(4):
            cr = x + dr[a]
            cc = y + dc[a]
            if cr <0 or cr >=R or cc<0 or cc >=C:continue
            if vis[cr][cc]: continue
            if A[cr][cc] != team: continue
            vis[cr][cc] =1
            queue.append([cr,cc])
    if team == 'W':
        W += cnt*cnt
    else:
        B += cnt*cnt

for i in range(R):
    for j in range(C):
        if vis[i][j] ==0:
            bfs(i,j,A[i][j])

print(f"{W} {B}")
