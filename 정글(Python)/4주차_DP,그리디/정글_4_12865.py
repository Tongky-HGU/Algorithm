#평범한 배낭
import sys
N, K = map(int,sys.stdin.readline().split())
A =[[0,0]]
for i in range(1,N+1):
    A.append(list((map(int,sys.stdin.readline().split()))))
def knapsack():
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,K+1):
            if A[i][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-A[i][0]]+A[i][1])
    print(dp[-1][-1])

knapsack()