import sys, heapq

N = int(sys.stdin.readline())
A = []
B = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    A.append([start,end])

A.sort(reverse=True)

i = 0
cnt = 0
available = 0
while(A):
    start, end = A.pop()
    if(B):
        while(B and B[0] <= start):
            heapq.heappop(B)
            available += 1
    if available > 0:
        heapq.heappush(B,end)
        available -= 1
    else:
        heapq.heappush(B,end)
        cnt +=1

print(cnt)