# 조합
import sys
# nCm = n! / n-m! * m!
N,M = map(int,sys.stdin.readline().split())
dp = [ 0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1
for i in range(2,N+1):
    dp[i] = dp[i-1]*i

print(dp[N]//(dp[N-M]*dp[M]))