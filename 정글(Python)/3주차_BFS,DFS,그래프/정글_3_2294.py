# 동전 2 
# dp로도 풀 수 있음
import sys
from collections import deque
N, K = map(int,sys.stdin.readline().split())

A =[]
queue = deque()
vis=[False for _ in range(K+1)]
for i in range(N):
    a = int(sys.stdin.readline())
    if a > K: continue
    A.append(a)
    queue.append(a)
    vis[a]=True

def sol():
    cnt = 0
    flag = False
    while(1):
        cursize = len(queue)
        while(cursize):
            cur = queue.popleft()
            if cur == K:
                flag = True
                break
            for i in range(len(A)):
                newcur = cur + A[i]
                if newcur > K: continue
                if vis[newcur]==True: continue
                queue.append(newcur)
                vis[newcur]=True
            cursize-=1
        cnt += 1
        if flag == True:
            print(cnt)
            break
        if len(queue) == 0:
            print(-1)
            break
sol()