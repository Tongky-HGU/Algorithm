#정수 삼각형
import sys
N = int(sys.stdin.readline())
dp =[[] for _ in range(N)]
for i in range(N):
	dp[i]=list(map(int,sys.stdin.readline().split()))
for i in range(1,N):
	dp[i][0] = dp[i][0] + dp[i-1][0]
	dp[i][i] = dp[i][i] + dp[i-1][i-1]
	for j in range(1,i):
		dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + dp[i][j] 
print(max(dp[N-1]))

	

