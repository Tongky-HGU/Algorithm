#블랙잭
import sys

N, M = map(int,sys.stdin.readline().split())

A = list(map(int,sys.stdin.readline().split()))
# A = sorted(A)
ans = 0;
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (A[i]+A[j]+A[k] <= M):
                ans = max(ans ,A[i]+A[j]+A[k])

print(ans)
    
