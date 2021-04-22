#인간 대포
import sys, heapq, math

def time_walk(a,b):
    dist = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    return dist/5

def time_canon(a,b):
    dist = abs(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5 - 50)
    return (dist/5) +2

X1, Y1 = map(float,sys.stdin.readline().split())
X2, Y2 = map(float,sys.stdin.readline().split())

N = int(sys.stdin.readline())
X = []*(N+2)
X.append([X1,Y1])
for _ in range(N):
    X.append(list(map(float,sys.stdin.readline().split())))
X.append([X2,Y2])
A = [[] for _ in range(N+2)]

for i in range(1,N+2):
    A[0].append([time_walk(X[0],X[i]),i])
    A[i].append([time_walk(X[0],X[i]),0])


for i in range(1,N+2):
    for j in range(i+1,N+2):
        A[i].append([min(time_walk(X[i],X[j]),time_canon(X[i],X[j])),j])
        A[j].append([min(time_walk(X[i],X[j]),time_canon(X[i],X[j])),i])

def dij():
    vis = [0 for _ in range(N+2)]
    time = [math.inf for _ in range(N+2)]
    queue = []
    time[0] = 0
    heapq.heappush(queue,[time[0],0])
    while(queue):
        _,cur = heapq.heappop(queue)
        if vis[cur]: continue
        vis[cur] = 1
        for d, to in A[cur]:
            time[to] = min(time[to],time[cur]+d)
            if not vis[to]:
                heapq.heappush(queue,[time[to],to])
    return time[-1]
    
print(dij())

import sys
a, b = map(int,sys.stdin.readline().split())
print(a-b)