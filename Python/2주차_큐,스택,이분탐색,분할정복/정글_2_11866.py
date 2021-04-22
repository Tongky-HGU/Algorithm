# 요세푸스 문제
# join

import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())

a = deque(i+1 for i in range(N))
ans = deque()

while(len(a)>0):
    a.rotate(-(K-1))
    ans.append(a.popleft())
    # for i in range(K):
    #     if i == K-1:
    #         ans.append(a[0])
    #         a.popleft()
    #     else:
    #         a.append(a[0])
    #         a.popleft()

print('<',end='')
for i in range(N-1):
    print(ans[i],end=', ')
print(str(ans[N-1])+'>')