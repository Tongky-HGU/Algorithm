# 추석트래픽
import heapq
from collections import deque

def timeToStartEnd(string):
    string = string.split(' ')
    start = 0
    time = list(map(float,string[1].split(':')))

    end = time[0]*60*60 + time[1]*60 + time[2]
    start = end - float(string[2][:-1]) +0.001
    return [end,start]

def solution(lines):
    queue = []
    for string in lines:
        queue.append(timeToStartEnd(string))

    queue.sort(key = lambda x : x[1])
    queue =deque(queue)
    # print(queue)
    ans = 0
    count = []
    while(queue):
        cur = queue.popleft()
        heapq.heappush(count,cur)
        while(count):
            if count[0][0] <= cur[1] - 1:
                heapq.heappop(count)
            else:
                break

        ans = max(ans,len(count))

    print(ans)
    return ans