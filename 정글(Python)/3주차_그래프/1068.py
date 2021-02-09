#트리
import sys

N = int(sys.stdin.readline())
A = list(sys.stdin.readline().split())
D = int(sys.stdin.readline())
X = {}

for i in range(N):
    if A[i] not in X:
        X[A[i]] = [i]
        continue
    X[A[i]].append(i)

ans = 0

# print(X)

def count(a):
    global ans
    if a == D: return
    if str(a) not in X:
        ans+=1
        return
    for child in X[str(a)]:
        count(child)

if A[D] == 0:
    print(ans)
else:
    count(-1)
    print(ans)

