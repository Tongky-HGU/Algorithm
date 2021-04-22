#소수경로
import sys, heapq, math
N = int(sys.stdin.readline())

def check(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

def bfs(a,b):
    vis = [math.inf for _ in range(10000)]
    queue = []
    heapq.heappush(queue,[0,a])
    vis[a] = 0;
    while(queue):
        cnt,cur = heapq.heappop(queue)
        # print(f"{cur} {cnt}")
        if cur == b:
            return cnt
        for i in range(0,4):
            for j in range(0,10):
                new = (cur // 10**(i+1) * 10**(i+1)) + (cur % 10**(i)) + (j * 10**i)
                if new < 1000 or cnt >= vis[new] or check(new) == False : continue
                vis[new] = cnt
                queue.append([cnt+1,new])
    return -1

for _ in range(N):
    A, B = map(int,sys.stdin.readline().split())
    ans = bfs(A,B)
    if ans == -1:
        print("Impossible")
    else: print(ans)
    