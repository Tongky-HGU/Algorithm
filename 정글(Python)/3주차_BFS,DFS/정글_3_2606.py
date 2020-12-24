#바이러스
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

C = [[0 for r in range(N)] for c in range(N)]

for _ in range(K):
    A,B = map(int,sys.stdin.readline().split())
    C[A-1][B-1] = 1
    C[B-1][A-1] = 1

queue =[]
vis=[0]*N

vis[0] = 1
queue.append(0)
cnt=0
while(1):
    cur = queue.pop(0)
    cnt+=1
    for i in range(N):
        if C[cur][i] == 1:
            if vis[i]==0:
                queue.append(i)
                vis[i] = 1
                
    if len(queue) == 0:
        break
print(cnt-1)