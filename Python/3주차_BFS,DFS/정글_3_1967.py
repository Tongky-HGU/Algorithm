#트리의지름
# a로부터 가장 먼점 b
# b로부터 가장 먼점 C 는 트리의 지름
import sys
from collections import deque

N = int(sys.stdin.readline())

A = [[] for _ in range(N+1)]

for _ in range(N-1):
    parent,child,d = map(int,sys.stdin.readline().split())
    A[parent].append([d,child])
    A[child].append([d,parent])

def bfs(i,mode):
    queue = deque()
    queue.append(i)
    vis = [-1 for _ in range(N+1)]
    vis[i] = 0 
    while(queue):
        cur = queue.popleft()
        
        for d, to in A[cur]:
            if vis[to] == -1:
                vis[to] = vis[cur] + d
                queue.append(to)
    if mode == 1:
        return vis.index(max(vis))
    else:
        return max(vis)

print(bfs(bfs(1,1),2))
