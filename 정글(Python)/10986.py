#나머지 합
import sys
N,M = map(int,sys.stdin.readline().split())

A = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(N+1)]
remain = [0 for _ in range(M)]
for i in range(1,N+1):
    dp[i] = (dp[i-1] + A[i-1]) % M
    remain[dp[i]] +=1

ans = 0
for i in range(M):
    if i ==0:
        #가우스 공식
        ans += ((remain[i] +1) * remain[i]) //2
    else:
        ans += (remain[i] * (remain[i]-1)) // 2
    
print(ans)