#토마토
import sys 
from collections import deque

M, N, K = map(int,sys.stdin.readline().split())

A = []
for _ in range(K):
    a = []
    for _ in range(N):
        a.append(list(map(int,sys.stdin.readline().split())))
    A.append(a)



vis = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K)]

# print(A)
# print(vis)

dx = [1,0,-1,0,0,0]
dy = [0,-1,0,1,0,0]
dz = [0,0,0,0,1,-1]
tomato = 0
cnt = 0
day = 0
queue = deque()

for i in range(K):
    for j in range(N):
        for k in range(M):
            if A[i][j][k] == 1:
                queue.append([i,j,k,0])
                vis[i][j][k] = 1
                cnt -= 1
            elif A[i][j][k] == 0:
                tomato +=1
def bfs():
    global day, cnt
    while(1):
        cur = queue.popleft()
        cnt +=1
        day = max(day,cur[3])
        # print(cur)
        for i in range(6):
            cx = cur[1] + dx[i]
            cy = cur[2] + dy[i]
            cz = cur[0] + dz[i]
            if cz < 0 or cz >= K or cx < 0 or cx >= N or cy < 0 or cy >= M: continue
            if vis[cz][cx][cy] == 1: continue
            if A[cz][cx][cy] == -1 or A[cz][cx][cy] == 1: continue
            queue.append([cz,cx,cy,cur[3]+1])
            vis[cz][cx][cy] = 1
        if len(queue) == 0:
            break

bfs()

if tomato == cnt:
    print(day)
else:
    print(-1)



        
    
    
