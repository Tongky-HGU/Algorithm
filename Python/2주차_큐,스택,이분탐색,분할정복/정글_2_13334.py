# 철로

import sys
import heapq

N = int(sys.stdin.readline())

a=[]
for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    if x[0] < x[1]:
        x[0],x[1] = x[1],x[0] 
    heapq.heappush(a,x)

L = int(sys.stdin.readline())

# print('*'*30)

ans = 0
on = []
while(len(a)>0):
    x = heapq.heappop(a)
    # print(x)
    cr = x[0]
    if x[0]-x[1] > L:
        continue
    else:
        heapq.heappush(on,x[1])
    while(len(on)>0):
        # print(on)
        if cr - on[0] <= L:
            break
        else:
            heapq.heappop(on)
    ans = max(ans,len(on))

print(ans)

