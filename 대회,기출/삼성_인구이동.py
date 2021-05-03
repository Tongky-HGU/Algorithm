#인구인동 
import sys
from collections import deque
N, L, R = map(int,sys.stdin.readline().split())
A = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

queue = deque()
ans = 0
while(1):
    flag = False
    ans += 1
    vis = [[0 for _ in range(N)] for _ in range(N)]
    temp = []

    for i in range(N):
        for j in range(N):
            if vis[i][j] == 1 : continue
            vis[i][j] = 1
            a, b = -1, -1
            if i != N-1:
                a = abs(A[i][j] - A[i+1][j])
            if j != N-1:
                b = abs(A[i][j] - A[i][j+1])

            if (a >= L and a <=R) or (b >= L and b <=R): 
                queue.append([i,j])
                temp = []
                flag = True
                sm = 0

            while(queue):
                x,y = queue.popleft()
                temp.append([x,y])
                sm += A[x][y]
                for k in range(4):
                    rr = x + dr[k]
                    cc = y + dc[k]
                    if rr < 0 or rr >= N or cc < 0 or cc >= N: continue
                    if vis[rr][cc] == 1: continue
                    if abs(A[rr][cc] - A[x][y]) < L or abs(A[rr][cc] - A[x][y]) > R: continue
                    vis[rr][cc] = 1
                    queue.append([rr,cc])
            
            if temp:
                avg = sm // len(temp)
                for x,y in temp:
                    A[x][y] = avg
    
    if not flag:
        break

print(ans -1)
             

    
    
    
