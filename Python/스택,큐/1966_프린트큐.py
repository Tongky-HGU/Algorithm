import sys
from collections import deque

test = int(sys.stdin.readline())

for _ in range(test):
    ans = 0
    N, M = map(int,sys.stdin.readline().split())
    A = deque(map(int,sys.stdin.readline().split()))
    I = deque(i for i in range(len(A)))
    I[M] = 101

    while(1):
        if A[0] == max(A):
            ans += 1
            if I[0] == 101:
                print(ans)
                break
            else:
                A.popleft()
                I.popleft()
        else:
            A.append(A.popleft())
            I.append(I.popleft())
