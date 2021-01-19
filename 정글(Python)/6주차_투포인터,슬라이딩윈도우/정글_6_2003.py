#수들의합
import sys
N, M = map(int,sys.stdin.readline().split())
A = [0] + list(map(int,sys.stdin.readline().split()))

cr = 0
cl = 0
sum1 =0
ans =0

while(cr<=N):
    # print(cl)
    # print(cr)

    if (sum1<=M) :
        if(sum1 == M):
            ans +=1
        if (cr == N):
            break
        cr +=1

        sum1 += A[cr]
    else:
        sum1 -= A[cl]
        cl +=1

    # print(ans)
    # print("---------------")

print(ans)



