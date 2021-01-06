#연속합
import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(N)]
for i in range(0,N):
	dp[i]= max(0,dp[i-1])+A[i]
print(max(dp))