#숫자 카드
import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

A = sorted(A)

for i in range(M):
    ans = 0
    cl = 0
    cr = N-1
    
    while(cl<=cr):
        mid =(cl+cr)//2
        if B[i] == A[mid]:
            ans = 1
            break
        elif B[i] > A[mid]:
            cl = mid+1
        else:
            cr = mid-1
    print(ans,end=" ")

