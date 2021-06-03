#웜홀
import sys,math
#웜홀,길 정보저장
T = int(sys.stdin.readline())
for _ in range(T):
    N, M, W = map(int,sys.stdin.readline().split())
    road = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b,d = map(int,sys.stdin.readline().split())
        road[a].append([b,d])
        road[b].append([a,d])
    for _ in range(W):
        a,b,d = map(int,sys.stdin.readline().split())
        road[a].append([b,-d])
    # print(road)

    # - 출발지점을 다르게 해서 dfs 로 탐색한다.
    # - 출발지점에 도착했는데 cnt가 -1 이라면 ans true로

    # + 벨만 포드
    # 나머지 노드 방문하며 주변 노드에 방문하는 최단거리 갱신 (v-1 번 반복)
    # 한 번 더 방문하면 업데이트 되는지 확인 (사이클 확인, 사이클이 있다면 false)
    # + math.inf 아닌지 확인하는 부분 없앰. 어차피 음수 사이클만 찾으면 됨
    vis = [math.inf for _ in range(N+1)]
    vis[N] = 0 # + 이거때문에 계속 실패하는 거엿음;;;; 0 하면 틀림
    ans = False
    for t in range (N):
        for i in range(1,N+1):
            for to, dist in road[i]:
                if vis[to] > vis[i]+dist:
                    vis[to] = vis[i]+dist
                    if t == N-1:
                        ans = True
        
    # print(vis)
    if ans:
        print("YES")
    else:
        print("NO")