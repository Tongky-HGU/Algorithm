#로또
import sys

def dfs(a,start):
    # print(a)
    if len(a) == 6:
        print(*a)
    for i in range(start,N):
        if vis[i] == 0 and len(a)<=6:
            vis[i]=1
            a.append(A[i])
            dfs(a,i)
            a.pop()
            vis[i]=0

while(1):
    A = list(map(int,sys.stdin.readline().split()))
    if A[0] == 0 :break
    N = A[0]
    A = A[1:]
    vis = [0 for _ in range(N)]
    dfs([],0)
    print()


    