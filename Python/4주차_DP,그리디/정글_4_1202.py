#보석도둑
import sys, heapq

N, K = map(int,sys.stdin.readline().split())
J = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
B = [int(sys.stdin.readline()) for _ in range(K)]

J.sort()
B.sort()

queue = []
i = 0
ans = 0
for weight in B:
    while(1):
        if i == N:
            if queue:
                max_price = heapq.heappop(queue)
                ans += -max_price
            break
        if weight >= J[i][0]:
            heapq.heappush(queue,-J[i][1])
        else:
            if queue:
                max_price = heapq.heappop(queue)
                ans += -max_price
            break
        i+=1

print(ans)