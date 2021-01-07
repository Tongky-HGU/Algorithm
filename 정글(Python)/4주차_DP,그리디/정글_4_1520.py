#내리막길
import sys, math
N, M = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# print("x"*24)
# for i in range(N):
#     print(A[i])

dr = [1,0,-1,0]
dc = [0,-1,0,1]

dp = [[-1 for _ in range(M)] for _ in range(N)]
dp[N-1][M-1] = 1
def dfs(i,j):
    if dp[i][j] >= 0:
        return dp[i][j]
    tmp = 0
    for x in range(4):
        cr = i +dr[x]
        cc = j +dc[x]
        if 0<=cr<N and 0<=cc<M and A[cr][cc] < A[i][j]:
            tmp += dfs(cr,cc)
    dp[i][j]=tmp
    return tmp
dfs(0,0)

# print("x"*24)
# for i in range(N):
#     print(dp[i])

print(dp[0][0])