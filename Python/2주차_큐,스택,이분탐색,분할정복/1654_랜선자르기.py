#랜선자르기
import sys 
N, M = map(int,sys.stdin.readline().split())
A =[]
for _ in range(N):
    A.append(int(sys.stdin.readline()))
# print(A)

cl = 1
cr = max(A)
ans = cl
while(cl<=cr):
    mid = (cl+cr)//2
    
    cnt = 0
    for i in range(N):
        cnt += A[i]//mid
    
    # print(f"{mid}  {cnt}")
    if cnt >= M:
        ans = max(ans,mid)
        cl = mid + 1
    else:
        cr = mid -1

print(ans)