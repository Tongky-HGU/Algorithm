#2xn 타일링
import sys
N = int(sys.stdin.readline())
if N == 1: print(1)
else:
    dp = [0 for _ in range(N)]
    dp[0], dp[1] = 1,2
    for i in range(2,N):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    print(dp[N-1])