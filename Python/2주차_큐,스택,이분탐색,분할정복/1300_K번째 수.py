#k번째수
import sys 
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

cl = 1
cr = N*N
ans = cr
while (cl <= cr):
    mid = (cl+cr)//2

    temp = 0
    for i in range(1,N+1):
        temp += min(N,mid//i)

    if temp >= K:
        ans = mid
        cr = mid-1
    else:
        cl = mid+1

print(ans)