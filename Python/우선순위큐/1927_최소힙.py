import heapq,sys

N = int(sys.stdin.readline())
A = []
for i in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(A) == 0:
            print(0)
        else:
            print(heapq.heappop(A))
    else:
        heapq.heappush(A,X)

