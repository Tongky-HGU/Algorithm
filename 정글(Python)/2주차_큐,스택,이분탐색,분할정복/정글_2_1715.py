# 카드 정렬하기
import sys
import heapq

N = int(sys.stdin.readline())
a=[]
for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(a,x)

if len(a) == 1:
    print(0)
else:
    ans=0
    while len(a) > 1:
        temp1= heapq.heappop(a)
        temp2= heapq.heappop(a)
        ans += temp1+temp2
        heapq.heappush(a,temp1+temp2)
    print(ans)