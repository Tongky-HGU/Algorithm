#트리
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
D = int(sys.stdin.readline())
X = {}

for i in range(N):
    if i == D or A[i] == D: continue
    if A[i] not in X:
        X[A[i]] = [i]
        continue
    X[A[i]].append(i)

ans = 0

# print(X)

def count(a):
    global ans
    if a not in X:
        ans+=1
        return
    for child in X[a]:
        count(child)

if -1 not in X:
    print(ans)
else:
    count(-1)
    print(ans)

