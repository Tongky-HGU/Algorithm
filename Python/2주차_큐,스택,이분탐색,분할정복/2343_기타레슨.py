#기타레슨
import sys
N,M = map(int,sys.stdin.readline().split())
A= list(map(int,sys.stdin.readline().split()))

cl = sum(A)//M 
cr = sum(A)
ans = cr

while(cl<=cr):
    mid = (cl+cr)//2

    if mid < max(A):
        cl =mid+1
        continue

    cnt = 0
    temp = 0
    for i in range(N):
        if A[i] > mid:
            break
        elif temp + A[i] <= mid:
            temp += A[i]
        else:
            temp = A[i]
            cnt += 1
        if cnt > M:
            break

    if cnt <= M -1:
        cr = mid - 1
        ans = min(ans,mid)
    else:
        cl = mid + 1
    # print(f"----------------")


print(ans)
    
