#신입사원
# 살펴보면 sort를 할 이유가 없었다...
import sys
def sol():
    N = int(sys.stdin.readline())
    A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    A.sort()
    ans = 1
    mini = A[0][1]
    for i in range(1,N):
        if A[i][1] < mini:
            ans += 1
            mini = A[i][1]
    print(ans)

T = int(sys.stdin.readline())
for _ in range(T):
    sol() 