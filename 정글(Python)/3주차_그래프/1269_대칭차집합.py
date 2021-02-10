#대칭차집합
import sys
N, M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

X = {}
for i in range(len(A)):
    X[A[i]] = 0

cnt = 0
ans = 0

for i in range(len(B)):
    if B[i] in X:
        cnt += 1
    else:
        ans += 1

ans = len(X) - cnt + ans
print(ans)

