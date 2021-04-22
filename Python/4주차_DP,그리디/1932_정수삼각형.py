# 정수삼각형
import sys

N = int(sys.stdin.readline())
dp = [[ -1 for _ in range(N)] for _ in range(2)]
dp[0][0] = int(sys.stdin.readline())

for i in range(1,N):
    A = list(map(int,sys.stdin.readline().split()))
    for j in range(i+1):
        if j == 0:
            dp[1][j] = A[j]+dp[0][j]
        elif j == i:
            dp[1][j] = A[j]+dp[0][j-1]
        else:
            dp[1][j] = max(A[j]+dp[0][j],A[j]+dp[0][j-1])

    dp[0][:] =dp[1][:]
print(max(dp[0]))
