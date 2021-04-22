# 공유기 설치

import sys 

n, x = list(map(int,sys.stdin.readline().split()))
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()

cl = 0
cr = a[n-1] - a[0]
ans = 0
while(cl <= cr):
    mid = (cl+cr)//2
    cnt = 1
    start = a[0]
    for i in range(n):
        if a[i] - start >= mid:
           cnt +=1
           start = a[i]
    if cnt >= x:
        ans = mid
        cl = mid +1 
    else:
        cr = mid -1

print(ans)