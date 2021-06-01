#N과M9
#  list(set(permutations(nums,M))) 쓰면됨...

import sys
N,M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
vis = [0 for i in range(N)]

# 재귀돌며 확인
def dfs(arr):
    # cnt = M 이면 return
    if len(arr) == M:
        # print(arr)
        print( " ".join([str(A[i]) for i in arr]))
        return
    
    used = {}

    for i in range(N):
        if vis[i] == 1: continue
        if A[i] in used:
            continue
        else:
            used[A[i]] = 1
            
        arr.append(i)
        vis[i] = 1
        dfs(arr)
        arr.pop()
        vis[i] = 0

for i in range(N):
    if i > 0 and A[i] == A[i-1]: continue
    vis[i] = 1
    dfs([i])
    vis[i] = 0
