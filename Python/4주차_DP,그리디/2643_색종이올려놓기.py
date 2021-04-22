#색종이올려놓기
import sys
N = int(sys.stdin.readline())
A = [sorted(list(map(int,sys.stdin.readline().split()))) for _ in range(N)]
A = sorted(A,key=lambda x:(x[0],x[1]) )
# print(A )
dp = [0 for _ in range(N)]
for i, a in enumerate(A):
    dp[i]=1
    for j in range(i):
        if a[1] >= A[j][1]:
            dp[i] = max(dp[j]+1,dp[i])
# print(dp)

print(max(dp))
