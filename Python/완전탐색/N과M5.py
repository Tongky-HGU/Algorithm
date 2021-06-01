#N과M5
#* Permutation쓰면 더 빠르더라...
import sys
N,M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
vis = [0 for _ in range(N)]

# 재귀돌며 확인
def dfs(arr):
    # cnt = M 이면 return
    if len(arr) == M:
        print( " ".join(map(str,arr)))
        return

    for i in range(N):
        if vis[i] == 1: continue
        arr.append(A[i])
        vis[i] = 1
        dfs(arr)
        arr.pop()
        vis[i] = 0

for i in range(N):
    vis[i] = 1
    dfs([A[i]])
    vis[i] = 0