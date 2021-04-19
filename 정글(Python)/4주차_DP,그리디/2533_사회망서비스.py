#사회망서비스
import sys,math
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
A = [[] for _ in range(N)]
dp = [[0,0] for _ in range(N)]
vis = [0 for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    A[a-1].append(b-1)
    A[b-1].append(a-1)

def dfs(num):

    vis[num] = 1
    dp[num][0] = 1
    dp[num][1] = 0

    for i in A[num]:
        if vis[i] == 0:
            dfs(i)
            dp[num][0] += dp[i][1]
            dp[num][1] += max(dp[i][0],dp[i][1])

dfs(0)
print(N-max(dp[0][0],dp[0][1]))