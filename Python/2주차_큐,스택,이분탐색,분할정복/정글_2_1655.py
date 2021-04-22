# 가운데를 말해요
import sys
import heapq

N = int(sys.stdin.readline())

maxi= []
mini =[]
for _ in range(N):
    x = int(sys.stdin.readline())
    if len(mini) == len(maxi):
        heapq.heappush(maxi,(-x,x))
    else:
        heapq.heappush(mini,(x,x))

    if mini and maxi[0][1] > mini[0][1]:
        temp_min = heapq.heappop(mini)[1]
        temp_max = heapq.heappop(maxi)[1]
        heapq.heappush(mini,(temp_max,temp_max))
        heapq.heappush(maxi,(-temp_min,temp_min))

    print(maxi[0][1])