#배열합치기
import sys,heapq
N1, N2 = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
A = A + B
heapq.heapify(A)
for i in range(N1+N2):
    print(heapq.heappop(A),end=" ")
print()