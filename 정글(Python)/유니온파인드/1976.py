#여행가자
import sys
# sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N+1)]

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
    parent[a] = b

for i in range(N):
    A = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if A[j] and i != j:
            union(i+1,j+1)

A = list(map(int,sys.stdin.readline().split()))
flag = True
for i in range(0,M-1):
    if find(A[i]) != find(A[i+1]):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
