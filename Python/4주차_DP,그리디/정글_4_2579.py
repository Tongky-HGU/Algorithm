# 계단오르기
import sys
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
if N == 1 : print(A[0])
else:
    dp = [[0,0] for _ in range(N)]
    dp[0] = [A[0],0]
    dp[1] = [A[1],A[1]+A[0]]
    for i in range(2,N):
        dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + A[i]
        dp[i][1] = dp[i-1][0] + A[i]
        # print(dp)

    print(max(dp[N-1][0],dp[N-1][1]))
