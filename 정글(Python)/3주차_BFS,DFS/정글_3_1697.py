#숨바꼭질
import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
vis = [0]*100001
queue = deque()
queue.append([N,0])

while(queue):
    cur, cnt = queue.popleft()
    if vis[cur]: continue
    vis[cur] = True
    if cur == K:
        print(cnt)
        break
    a = [cur*2,cur+1,cur-1]

    for i in a:
        if i >= 0 and i <= 100000:
            queue.append([i,cnt+1])