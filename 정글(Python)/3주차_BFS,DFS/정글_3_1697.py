#숨바꼭질
import sys, math
from collections import deque

N, K = map(int,sys.stdin.readline().split())

def bfs():
    vis = [0]*100001
    queue = deque()
    queue.append([N,0])

    while(queue):
        cur,cnt = queue.popleft()
        if vis[cur]: continue
        if cur == K:
            print(cnt)
            return
        vis[cur]=1
        L = [cur*2, cur+1,cur-1]
        for l in L:
            if l < 0 or l >100000 : continue
            if vis[l]:continue
            queue.append([l,cnt+1])
            
bfs()