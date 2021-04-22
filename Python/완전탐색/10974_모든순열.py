#모든 순열
import sys
N = int(sys.stdin.readline())
vis =[0 for _ in range(N+1)]

def dfs(a):
    # print(a)
    if (len(a)==N):
        # print(" ".join(a))
        print(*a)
        return
    for i in range(1,N+1):
        # print(i)
        if vis[i] == 0:
            a.append(i)
            vis[i] = 1
            dfs(a)
            vis[i] = 0
            a.pop()

dfs([])

            
        