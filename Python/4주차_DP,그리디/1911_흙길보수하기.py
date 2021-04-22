#흙길보수하기
import sys,heapq
N,L = map(int,sys.stdin.readline().split())
ans = 0
now = 1
queue = []
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    queue.append([a,b])
queue = sorted(queue)
for i in range(N):
    a,b = queue[i]
    if now < a:
        now = a
    while(now < b):
        now += L
        ans += 1                                          

print(ans)