#소수의 곱
import sys
import heapq

K, N = list(map(int,sys.stdin.readline().split()))
A = list(map(int,sys.stdin.readline().split()))

print(K)
print(A)

heap1 = A[:]
for _ in range(N):
    head = heapq.heappop(heap1)

    for i in range(K):
        heapq.heappush(heap1,A[i]*head)
        if (head % A[i] == 0):
            break
print(head)
        
        