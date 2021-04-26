#센서
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = []
A.sort()
for i in range(len(A)-1):
    B.append(A[i+1]-A[i])
B.sort()
ans = 0
for i in range(N-K):
    ans += B[i]
print(ans)