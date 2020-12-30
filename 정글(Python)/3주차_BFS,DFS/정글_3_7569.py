#토마토
import sys 
from collections import deque

M, N = map(int,sys.stdin.readline().split())

A = []*N

for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

vis = [[0 for _ in range(M)] for _ in range(N)]

# print(A)
# print(vis)

dx = [1,0,-1,0]
dy = [0,-1,0,1]
tomato = 0
cnt = 0
day = 0
queue = deque()

for i in range(N):
    for j in range(M):
        if A[i][j] == 1:
            queue.append([i,j,0])
            vis[i][j] = 1
            cnt -= 1
        elif A[i][j] == 0:
            tomato +=1

def bfs():
    global day, cnt
    while(1):
        cur = queue.popleft()
        cnt +=1
        day = max(day,cur[2])
        # print(cur)
        for i in range(4):
            cx = cur[1] + dx[i]
            cy = cur[0] + dy[i]
            if cy < 0 or cy >= N or cx < 0 or cx >= M: continue
            if vis[cy][cx] == 1: continue
            if A[cy][cx] == -1 or A[cy][cx] == 1: continue
            queue.append([cy,cx,cur[2]+1])
            vis[cy][cx]  = 1
        if len(queue) == 0:
            break

bfs()

if tomato == cnt:
    print(day)
else:
    print(-1)



        
    
    
