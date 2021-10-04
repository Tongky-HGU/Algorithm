import heapq


def solution(n, edges):
    road = [[] for _ in range(n+1)]
    vis = [0 for _ in range(n+1)]

    for edge in edges:
        a, b = edge
        road[a].append(b)
        road[b].append(a)

    stack = [[1, 1]]

    while stack:
        dist, cur = heapq.heappop(stack)
        if vis[cur] != 0:
            continue
        vis[cur] = dist
        for i in road[cur]:
            if vis[i] != 0:
                continue
            heapq.heappush(stack, [dist+1, i])

    maximum = max(vis)
    return len(list(filter(lambda x: x == maximum, vis)))
