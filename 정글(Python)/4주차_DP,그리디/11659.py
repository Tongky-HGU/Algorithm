#구간합배열4
import sys 
N, M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = [0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i] = B[i-1] + A[i-1]

for _ in range(M):
    X ,Y = map(int,sys.stdin.readline().split())
    print(B[Y]-B[X-1])