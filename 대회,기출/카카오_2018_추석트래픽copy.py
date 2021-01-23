# 추석트래픽
import heapq
def solution(lines):
    A = []
    for line in lines:
        a = line.split()[1:]
        b = a[0].split(':')
        b = int(b[0])*3600+int(b[1])*60+float(b[2])
        c = b - float(a[1][0:-1]) + 0.001
        A.append([b,c])
    
    A.sort(key = lambda x: x[1])
    
    queue=[]
    ans = 0
    for i in range(len(A)):
        heapq.heappush(queue,A[i][0])
        
        while queue and A[i][1]- queue[0]  >= 1:
            heapq.heappop(queue)
            
        ans = max(ans,len(queue))

    return ans