#알파벳
import sys

R,C = map(int,sys.stdin.readline().split())

A = []
for _ in range(R):
    A.append(list(map(ord,sys.stdin.readline().rstrip())))

vis = [0]*(ord('Z')-ord('A')+1)

dr = [1,0,-1,0]
dc = [0,-1,0,1]

def dfs(r,c,cnt):
    global maxi
    # print(chr(A[cur[0]][cur[1]]))
    maxi = max(maxi,cnt)
    vis[A[r][c]-65] = 1
    for i in range(4):
        cr= r+dr[i]
        cc= c+dc[i]
        if cr < 0 or cr >= R or cc < 0 or cc >= C : continue
        if vis[A[cr][cc]-65] == 1 : continue
        vis[A[cr][cc]-65] = 1
        dfs(cr,cc,cnt+1)
        vis[A[cr][cc]-65] = 0

maxi = 0
vis[A[0][0]-65] = 1
dfs(0,0,1)

print(maxi)


    
