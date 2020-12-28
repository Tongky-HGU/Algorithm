# 빙산
import sys
from collections import deque

R, C = map(int,sys.stdin.readline().split())
A= []
for i in range(R):
    A.append(list(map(int,sys.stdin.readline().split())))

dr = [0,1,0,-1]
dc = [1,0,-1,0]
hour = 0
def sol():
    global hour
    while(1):
        vis=[[0 for _ in range(C)] for _ in range(R)] 
        stack = deque()
        cnt = 0
        vis_cnt = 0
        for i in range(1,R-1):
            for j in range(1,C-1):
                if A[i][j] > 0:
                    cnt +=1
                    if len(stack) == 0:
                        stack.append([i,j])
                        vis[i][j] = 1
        if len(stack) > 0:
            while(1):
                cur = stack.pop()
                vis_cnt +=1
                for i in range(4):
                    cr = cur[0] + dr[i]
                    cc = cur[1] + dc[i]
                    if cr < 0 or cr >= R or cc < 0 or cc >= C: continue
                    if vis[cr][cc] == 1 : continue
                    # if A[cr][cc] == 0 and A[cur[0]][cur[1]]>0:
                    if A[cr][cc] == 0:
                        if A[cur[0]][cur[1]] > 0:
                            A[cur[0]][cur[1]] -= 1
                        continue

                    vis[cr][cc] =1
                    stack.append([cr,cc])
                if len(stack) == 0:
                    break

        hour+=1

        if cnt == 0:
            print(0)
            break

        elif cnt > vis_cnt:
            print(hour-1)
            break

sol()
