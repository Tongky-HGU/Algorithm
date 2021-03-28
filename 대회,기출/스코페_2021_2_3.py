import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
A = [[] for _ in range(N+1)]
# print(A)

for _ in range(N-1):
    a, b = map(int,sys.stdin.readline().split())
    A[a].append(b)

queue = deque()

for _ in range(M):
    success =False
    a, b = map(int,sys.stdin.readline().split())
    queue.append(a)
    while(queue):
        cur = queue.pop()
        if cur == b:
            success = True
            break
        for child in A[cur]:
            queue.append(child)
    if success:
        print("yes")
    else:
        print("no")