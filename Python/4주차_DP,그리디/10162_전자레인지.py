# 전자레인지
import sys
N = int(sys.stdin.readline())
A = [300,60,10]
ans = [0 for _ in range(3)]
cnt = 0

for i in range(3):
    if N // A[i]:
        ans[i] = N // A[i]
        N = N % A[i]

if N == 0:
    print(*ans) 
else:
    print(-1)
