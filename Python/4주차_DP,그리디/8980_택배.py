#택배
import sys,heapq
from collections import deque

N, C = map(int,sys.stdin.readline().split())
M = int(sys.stdin.readline())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
A.sort(key=lambda x : [x[1],x[0]])

# print(A)

ans = 0
B = [C]*(N+1)

for i in range(M):
    temp = C
    for j in range(A[i][0],A[i][1]):
        temp = min(temp, B[j])
    temp = min(temp,A[i][2])
    for j in range(A[i][0],A[i][1]):
        B[j] -= temp
    ans += temp
    # print(B)

print(ans)
