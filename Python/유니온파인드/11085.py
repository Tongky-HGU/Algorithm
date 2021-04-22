#군사이동
import sys
import heapq

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a >= b:
        parent[a] = b
    else:
        parent[b] = a
    return

p, w = map(int,sys.stdin.readline().split())
c, v = map(int,sys.stdin.readline().split())

parent = [i for i in range(p)]
queue = []

for _ in range(w):
    w1, w2, w = map(int,sys.stdin.readline().split())
    w= -w
    heapq.heappush(queue,[w, [w1,w2]])

while(queue):
    w,road = heapq.heappop(queue)
    union(road[0],road[1])
    if find(c) == find(v):
        print(-w)
        break        

