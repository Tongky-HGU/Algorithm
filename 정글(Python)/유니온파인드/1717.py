#집합의 표현
import sys
sys.setrecursionlimit(10**5)

def find(a):
    global parent
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a] 

def union(a,b):
    global parent

    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[a] = b

N, M = map(int,sys.stdin.readline().split())

parent = [i for i in range(N+1)]

for _ in range(M):
    X, A, B = map(int,sys.stdin.readline().split())
    if X:
        if find(A) == find(B):
            print("YES")
        else:
            print("NO")
    else:
        union(A,B)