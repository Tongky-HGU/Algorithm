#제자리 멀리뛰기
import sys 

D, N, M = map(int,sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)] + [D]
A.sort()

cl = 0
cr = D
ans=0
while cl<=cr:
    cnt = 0
    mid = (cl+cr)//2
    before = 0
    for i in A:
        if i - before >= mid:
            cnt += 1
            before = i

    if cnt >= N-M+1:
        ans = max(ans,mid)
        cl = mid + 1
    else:
        cr = mid -1
    
    # print(cl,cr)

print(ans)



            
