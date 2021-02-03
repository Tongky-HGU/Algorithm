#친구비
import sys

N, M, K = map(int,sys.stdin.readline().split())

parent = [i for i in range(N+1)]

L = [0] + list(map(int,sys.stdin.readline().split()))

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    
    if L[a] >= L[b]:
        L[a] = L[b]
        parent[a] = b
    else:
        L[b] = L[a]
        parent[b] = a
    return

for _ in range(M):
    A, B = map(int,sys.stdin.readline().split())
    union(A,B)


SET = set([find(i) for i in parent])
ans = 0

for i in SET:
    if i == 0: continue
    ans += L[i]

if ans > K:
    print("Oh no")
else:
    print(ans)



