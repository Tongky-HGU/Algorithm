import heapq

def solution(n, works):
    ans = 0
    queue= []
    for work in works:
        heapq.heappush(queue,-work)

    for _ in range(n):
        n = heapq.heappop(queue)
        heapq.heappush(queue,n+1)

    for x in queue:
        if x >= 0: continue
        ans += x**2

    return ans

print(solution(4,[4, 3, 3]))