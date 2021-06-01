#N과M2
import sys
N,M = map(int,sys.stdin.readline().split())
# 재귀돌며 확인
def dfs(A,cnt):
    # cnt = M 이면 return
    if cnt == M:
        print( " ".join(map(str,A)))
        # print(*A)
        return

    for i in range(A[-1]+1,N+1):
        A.append(i)
        dfs(A,cnt+1)
        A.pop()

for i in range(1,N+1):
    dfs([i],1)