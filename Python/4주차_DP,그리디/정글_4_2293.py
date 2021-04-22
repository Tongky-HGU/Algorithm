#동전1
import sys
N, K = map(int,sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0 for _ in range(K+1)]
dp[0] = 1
for i in range(0,N):
	for j in range(1,K+1):
		if j >= A[i]:
			dp[j] = dp[j-A[i]] + dp[j]
	# print(dp)
print(dp[K])

