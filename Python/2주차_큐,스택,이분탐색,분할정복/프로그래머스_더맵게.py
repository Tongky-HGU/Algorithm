#더맵게
import sys
import heapq

def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    while(1):
        a = heapq.heappop(scoville)
        if (a >= K):
            break
        if not(scoville):
            ans = -1
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,(a+(2*b)))
        ans+=1
    return ans

