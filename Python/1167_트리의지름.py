#트리의 지름
import sys

# 간선정보 저장
N = int(sys.stdin.readline())
A = [[] for _ in range(N+1)]
for _ in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    i = temp[0]
    idx = 1
    while temp[idx] != -1:
        A[i].append([temp[idx+1],temp[idx]])
        idx += 2

# - 내림차순 sort 후 

# 거리가 긴 순으로 방문
# - 시작 위치에 따라 다를수도
# + 먼저 가장 먼 노드를 구하고, 그 노드에서 가장 먼 노드를 재면 최대
def dfs(start,cur,cnt,result):
    for d, to in A[cur]:
        if result[to] == 0 and to != start:
            result[to] = result[cur]+d
            dfs(start,to,cnt+d,result)

result1 = [0 for _ in range(N+1)]
dfs(1,1,0,result1)
result1[1] = 0

# + 먼저 가장 먼 노드를 구하고, 그 노드에서 가장 먼 노드를 재면 최대
startNode = 0
mx = max(result1)
for i in range(N+1):
    if result1[i] == mx:
        startNode = i
        break

result2 = [0 for _ in range(N+1)]
dfs(startNode,startNode,0,result2)
result2[startNode] = 0
print(max(result2))