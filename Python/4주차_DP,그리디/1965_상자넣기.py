#상자넣기
import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp = [1 for _ in range(N)]
for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1) 
print(max(dp))