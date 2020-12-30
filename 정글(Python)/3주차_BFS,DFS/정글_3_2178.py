#미로탐색
import sys 

N, M = map(int,sys.stdin.readline().split())

A = [0]*N

for i in range(N):
    A[i] = list(map(int,sys.stdin.readline().rstrip()))
    
queue =[]
vis=[[0 for i in range(M)] for j in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

vis[0][0] = 1

queue.append([0,0,1])
while(1):
    cur = queue.pop(0)
    for i in range(4):
        cx = cur[0]+dx[i]
        cy = cur[1]+dy[i]
        if cx < 0 or cx >= N or cy < 0 or cy >= M :  continue
        if vis[cx][cy] == 1: continue
        if A[cx][cy] == 0: continue
        queue.append([cx,cy,cur[2]+1])
        vis[cx][cy] = 1
    if len(queue)==0 or (cur[0] == N-1 and cur[1] == M-1):
        print(cur[2])
        break


