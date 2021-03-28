import sys,math
N  = int(sys.stdin.readline())
# 거리 정리
dist = [[0 for _ in range(N)] for _ in range(N)]
A = {}
for _ in range(N):
    a, b, d = map(str,sys.stdin.readline().split())
    if a not in A:
        A[a] = len(A)
    if b not in A:
        A[b] = len(A)
    dist[A[a]][A[b]] = int(d)
    dist[A[b]][A[a]] = int(d)
# print(A)
# print(dist)

#dfs
ans = math.inf
# vis = [0 for _ in range(len(A))]
all_visited = 0
for i in range(len(A)):
    all_visited = all_visited | 1 << i 

def dfs(a,visit_cnt,cnt):
    global ans
    if cnt >= ans:
        return
    if visit_cnt & all_visited == all_visited:
        # print(vis)
        ans = min(ans,cnt)
        return
    for i in range(len(A)):
        if visit_cnt & 1<<i == 0:
            if visit_cnt == 0:
                dfs(i,visit_cnt | 1<<i,cnt) 
            else:
                dfs(i,visit_cnt | 1<<i,cnt + dist[a][i])

dfs(0,0,0)

print(ans)
    