#벽부수고이동하기
import sys, math
from collections import deque

R, C = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(R)]
dp =[[[math.inf ,math.inf]for _ in range(C)] for _ in range(R)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

queue = deque()
queue.append([0,0,1])
dp[0][0][1] = 1

while(queue):
    r,c,wall = queue.popleft()
    # print(f"{r} {c} {wall}")

    if r == R-1 and c == C-1 : break
    for i in range(4):
        cr = r + dr[i]
        cc = c + dc[i]
        if cr >= 0 and cr < R and cc >= 0 and cc < C:
            if dp[cr][cc][wall] != math.inf : continue
            if A[cr][cc] == 1:
                if wall == 0:
                    continue
                else:
                    dp[cr][cc][0] = dp[r][c][1] +1
                    queue.append([cr,cc,0])
            else:
                dp[cr][cc][wall] = dp[r][c][wall] +1
                queue.append([cr,cc,wall])

if min(dp[-1][-1][0],dp[-1][-1][1])  == math.inf:
    print(-1)
else:
    print(min(dp[-1][-1][0],dp[-1][-1][1]))
    

