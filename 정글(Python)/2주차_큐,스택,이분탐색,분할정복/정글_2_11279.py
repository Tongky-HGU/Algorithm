import sys
import heapq

N = int(sys.stdin.readline())
a=[]
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(a) == 0:
            print(0)
        else:
            temp = heapq.heappop(a)
            print(temp[1])
    else:
        temp = [-x, x]
        heapq.heappush(a,temp)