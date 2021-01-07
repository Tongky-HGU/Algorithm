#계단오르기 
import sys 
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
dp = [[0, 0] for _ in range(N+1)]
dp[1][0], dp[1][1] = A[0],A[0]
for i in range(2,N+1):
    dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + A[i-1]
    dp[i][1] = dp[i-1][0] + A[i-1]
print(max(dp[N]))