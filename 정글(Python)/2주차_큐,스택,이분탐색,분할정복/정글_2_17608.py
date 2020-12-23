# 막대기
import sys
n = int(sys.stdin.readline())
a=[]
for i in range(n):
    a.append(int(sys.stdin.readline()))

high = a[len(a)-1]
cnt = 1
for i in range(n-1,-1,-1):
    if(a[i]>high):
        cnt+=1
        high = a[i]
    
print(cnt)