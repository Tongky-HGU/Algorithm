#동전0
import sys
N, K = map(int,sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
for i in range(N-1,-1,-1):
    t = K // A[i]
    cnt += t
    K -= t*A[i]
print(cnt)
