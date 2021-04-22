#색상환
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

def dfs(n,k):
    # print(f"{n} {k}")
    if k == 1 :
        return n
    elif n/k == 2:
        return 2
    else:
        if dp[n][k] != 0:
            return dp[n][k]
        else:
            dp[n][k] = (dfs(n-1,k) + dfs(n-2,k-1))
            return dp[n][k] 
    
if N/2 < K:
    print(0)
else: 
    print(dfs(N,K)  % (10**9 +3))

