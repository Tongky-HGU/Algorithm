#로봇청소기
import sys
from collections import deque
R,C = map(int,sys.stdin.readline().split())
X,Y,D = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]

vis = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if A[i][j] == 1:
            vis[i][j] = 1

queue = deque()
queue.append([X,Y,D])
ans = 0 

D = [[-1,0],[0,1],[1,0],[0,-1]]

while(queue):
    x,y,d = queue.popleft()
    flag = 0 
    if vis[x][y] == 0:
        vis[x][y] = 1
        ans += 1
    for _ in range(4):
        d -= 1
        if d == -1: d = 3
        xx = x + D[d][0]
        yy = y + D[d][1]
        # print([xx,yy,d])
        if xx >= R or xx < 0 or yy >= C or yy < 0: continue
        if vis[xx][yy] == 1: continue
        queue.append([xx,yy,d])
        flag = 1
        break
    if not flag:
        xx = x - D[d][0]
        yy = y - D[d][1]
        if xx >= R or xx < 0 or yy >= C or yy < 0: break
        if A[xx][yy] == 1: break
        queue.append([xx,yy,d])
    # print(ans)

print(ans)
        
                
        



