# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    ans = -1
    queue = []
    for i in range(len(food_times)):
        heapq.heappush(queue,[food_times[i],i])
    left = k
    pre = 0
    while(queue):
        cur,idx = heapq.heappop(queue)
        
        if left - (cur-pre)*(len(queue)+1) >= 0:
            left -= (cur-pre)*(len(queue)+1)
            pre = cur
        else:
            queue.append([cur,idx])
            queue = sorted(queue,key = lambda x:x[1])
            ans = queue[left%len(queue)][1] +1
            break
        
        # print(left)
    
    return ans