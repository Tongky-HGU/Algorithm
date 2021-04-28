#로프
import sys
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort(reverse=True)
mx = 0
for i in range(N):
    mx =  max(mx,A[i]*(i+1))

print(mx)