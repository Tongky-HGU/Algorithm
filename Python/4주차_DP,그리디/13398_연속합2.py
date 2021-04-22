#연속합2
import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
# print(A)
dp=[[0, 0] for _ in range(N)] 
dp[0] = [A[0], -1000]
ans = A[0]
for i in range(1,N):
    dp[i][0] = max(dp[i-1][0]+A[i], A[i])
    dp[i][1] = max(dp[i-1][1]+A[i], dp[i-1][0])
    ans = max(dp[i][0],dp[i][1],ans)
print(ans)