#팰린드롬 만들기
import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [[-1 for _ in range(N)] for _ in range(N)]

def dfs(a,b):
    # print(f"{a} {b}")
    if a >= b:
        # dp[a][b] = 0
        return 0
    if dp[a][b] != -1:
        return dp[a][b]
    if A[a] == A[b]:
        dp[a][b] = dfs(a+1,b-1)
    else:
        dp[a][b] = min(dfs(a+1,b),dfs(a,b-1)) + 1
    
    return dp[a][b]

# for i in range(N-1):
#     for j in range(i+1,N):
#         dfs(i,j)

print(dfs(0,N-1))