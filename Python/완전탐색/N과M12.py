#N과M12
# set( combinations_with_replacement(arr, m))

import sys
N,M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.sort()

# 재귀돌며 확인
def dfs(arr):
    # cnt = M 이면 return
    if len(arr) == M:
        # print(arr)
        print( " ".join([str(A[i]) for i in arr]))
        return
    
    used = set()

    for i in range(arr[-1],N):
        if A[i] in used:
            continue
        else:
            used.add(A[i])
        arr.append(i)
        dfs(arr)
        arr.pop()

used = set()
for i in range(N):
    if A[i] in used:
        continue
    else:
        used.add(A[i])
    dfs([i])
