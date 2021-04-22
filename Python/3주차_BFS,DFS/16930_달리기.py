#달리기
import sys, math
from collections import deque
R, C, K = map(int,sys.stdin.readline().split())
A = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
vis = [[math.inf for _ in range(C)] for _ in range(R)]
R1, C1, R2, C2 = map(int,sys.stdin.readline().split())
R1 -= 1
C1 -= 1
R2 -= 1
C2 -= 1

dr = [-1,0,1,0]
dc = [0,1,0,-1]

queue = deque()
queue.append([R1,C1,4,0])
vis[R1][C1] = 0

while(queue):
    r,c,d,cnt = queue.popleft()
    # print(f"{r} {c} {d} {cnt}")
    if r == R2 and c == C2: 
        print(vis[R2][C2])
        exit()
    for i in range(4):
        cr = r + dr[i]
        cc = c + dc[i]
        if cr >= 0 and cr < R and cc >= 0 and cc < C:
            if A[cr][cc] == "#": continue
            if vis[cr][cc] <= vis[r][c]: continue
            if i != d or cnt == K :
                vis[cr][cc] = vis[r][c] +1
                cnt = 0
            else:
                vis[cr][cc] = vis[r][c]
            queue.append([cr,cc,i,cnt+1])

# for i in range(R):
    # print(vis[i])

print(-1)