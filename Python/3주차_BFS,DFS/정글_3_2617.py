# 구슬 찾기
import sys
from collections import deque   

N, M = map(int,sys.stdin.readline().split())

B = [[] for _ in range(N+1)]
S = [[] for _ in range(N+1)]

for _ in range(M):
    a = list(map(int,sys.stdin.readline().split()))
    S[a[0]].append(a[1])
    B[a[1]].append(a[0])

# print(S)
# print(B)

stack = deque()
ans = 0
half = (N+1)//2

def dfs_B(i):
    global cnt_B,vis
    cnt_B += 1
    vis[i] = 1
    for j in range(len(B[i])):
        if vis[B[i][j]] == 1:continue
        dfs_B(B[i][j])
        
def dfs_S(i):
    global cnt_S,vis
    cnt_S += 1
    vis[i] = 1
    for j in range(len(S[i])):
        if vis[S[i][j]] == 1:continue
        dfs_S(S[i][j])

for i in range(1,N+1):
    vis = [0 for _ in range(N+1)]
    cnt_B = 0    
    dfs_B(i)

    vis = [0 for _ in range(N+1)]
    cnt_S = 0    
    dfs_S(i)

    if cnt_B > half or cnt_S > half:
        ans +=1

print(ans)   