#로프
import sys, math
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort(key=lambda x: -x)
ans = 0
for i in range(len(A)):
    ans = max(ans,A[i]*(i+1))
print(ans)
    