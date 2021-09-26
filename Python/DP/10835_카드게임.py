import sys
N = int(sys.stdin.readline())

L = list(map(int,sys.stdin.readline().split()))
R = list(map(int,sys.stdin.readline().split()))

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if R[j] < L[i]:
            dp[i][j] = max(dp[i][j+1]+R[j] , dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])