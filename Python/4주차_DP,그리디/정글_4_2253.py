# 점프
import sys, math
N, M = map(int,sys.stdin.readline().split())
limit = int((2*N)**0.5)+1
dp = [[math.inf for _ in range(limit+1)] for _ in range(N+1)]
dp[2][1] = 1
for _ in range(M):
    dp[int(sys.stdin.readline())] = [-1 for _ in range(limit+1)]

# for i in range(N+1):
#     print(dp[i])

for i in range(N):
    for j in range(limit+1):
        if dp[i][j]==math.inf or dp[i][j] == -1 : continue
        if i+j <= N:
            dp[i+j][j] = min(dp[i+j][j],dp[i][j]+1)
        if i+j+1 <= N:
            dp[i+j+1][j+1] = min(dp[i+j+1][j+1],dp[i][j]+1)
        if j-1 > 0 and i+j-1 <= N:
            dp[i+j-1][j-1] = min(dp[i+j-1][j-1],dp[i][j]+1)

# print('*'*24)
# for i in range(N+1):
#     print(f"{i}{dp[i]}")

if min(dp[N]) == math.inf:
    print(-1)
else:
    print(min(dp[N]))


