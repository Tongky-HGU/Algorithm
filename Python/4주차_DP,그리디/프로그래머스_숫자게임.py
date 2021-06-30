#숫자 게임 
import heapq

def solution(A, B):
    ans = 0
    heapq.heapify(A)
    heapq.heapify(B)
    while(B):
        if A[0] < B[0]:
            heapq.heappop(A)
            heapq.heappop(B)
            ans += 1
        else:
            heapq.heappop(B)
    
    return ans

print(solution([5,1,3,7],[2,2,6,8]))