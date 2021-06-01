#N과M8
#* itertools.combinations_with_replacement 쓰면 더빠름
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

    for i in range(arr[-1],N):
        arr.append(i)
        dfs(arr)
        arr.pop()

for i in range(N):
    dfs([i])