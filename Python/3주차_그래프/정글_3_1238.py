#파티
import sys , heapq, math

N, M, X = map(int,sys.stdin.readline().split())
A =[[] for _ in range(N+1)]
B =[[] for _ in range(N+1)]


for _ in range(M,):
    a,b,t = map(int,sys.stdin.readline().split())
    A[a].append([t,b])
    B[b].append([t,a])

def dijkstra(a,array):
    time = [math.inf for _ in range(N+1)]
    vis=[0 for _ in range(N+1)]
    queue = []
    time[a] = 0
    heapq.heappush(queue,[time[a],a])
    while(queue):
        _,cur = heapq.heappop(queue)
        if vis[cur]: continue
        vis[cur]=1
        for t, to in array[cur]:
            time[to] = min(time[to],time[cur]+t)
            if not vis[to]:
                heapq.heappush(queue,[time[to],to])
    return time

max_time = 0
time_come = dijkstra(X,A)
time_go = dijkstra(X,B)

for i in range(1,N+1):
    time_need = time_go[i]+time_come[i]
    # if time_need == math.inf: continue
    max_time = max(max_time,time_need)

print(max_time)