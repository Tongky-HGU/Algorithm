#파도반 수열
import sys
N = int(sys.stdin.readline())
for _ in range(N):
	A = int(sys.stdin.readline())
	dp = [0 for _ in range(A)]
	if A == 1:
		print(1)
	elif A == 2:
		print(1)
	else:
		dp[0],dp[1],dp[2] = 1,1,1
		for i in range(3,A):
			dp[i] = dp[i-2] + dp[i-3]
		print(dp[A-1])