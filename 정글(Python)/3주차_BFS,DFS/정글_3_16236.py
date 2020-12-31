#아기상어
import sys, math
from collections import deque
N = int(sys.stdin.readline())
A=[]
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

# print(A)

def bfs(i,j,size):
    dr = [-1,0,0,1]
    dc = [0,-1,1,0]
    vis = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([i,j,0])
    vis[i][j]=1
    ans = 0
    eat = 0
    checklist = []
    
    while(queue):
        for _ in range(len(queue)):
            cur_r,cur_c,cnt = queue.popleft()
            # print(str(cur_r) + " " + str(cur_c)+"size="+str(size))
            # for i in range(N):
            #     print(vis[i])
            for i in range(4):
                cr ,cc = cur_r + dr[i], cur_c + dc[i]
                if cr < 0 or cr >= N or cc < 0 or cc >= N: continue
                if vis[cr][cc]: continue
                if A[cr][cc] > 0:
                    if A[cr][cc] > size: continue
                    elif A[cr][cc] < size:
                        checklist.append([cr,cc,cnt+1])
                vis[cr][cc] =1
                queue.append([cr,cc,cnt+1])

        if checklist:    
            # print(checklist)
            checklist.sort(key=lambda x: (x[0],x[1]))
            cr,cc,cnt = checklist[0]
            # print("eat "+str(cr) + " " + str(cc))
            eat += 1
            ans = cnt
            if eat == size:
                eat = 0
                size +=1
            A[cr][cc] = 0
            vis = [[0 for _ in range(N)] for _ in range(N)]
            queue.clear()
            vis[cr][cc] =1
            queue.append([cr,cc,cnt])
            checklist.clear()

    return ans


for i in range(N):
    for j in range(N):
        if A[i][j] == 9:
            A[i][j] = 0
            print(bfs(i,j,2))
            break
