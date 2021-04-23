#행성 터널
import sys, math
N = int(sys.stdin.readline())
A = [list(map(int,sys.stdin.readline().split())) + [i]  for i in range(N)]
B = []
vis = [i for i in range(N)]
ans = 0

def find(a):
    if vis[a] == a:
        return a
    vis[a] = find(vis[a])
    return vis[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    
    vis[a] = b
    return True

def kruskal():
    global ans
    for w, a, b in B:
        if union(a,b):
            ans+=w

A.sort()    
for i in range(N-1):
    B.append((abs(A[i][0]-A[i+1][0]),A[i][3],A[i+1][3]))
A.sort(key = lambda x : x[1])    
for i in range(N-1):
    B.append((abs(A[i][1]-A[i+1][1]),A[i][3],A[i+1][3]))
A.sort(key = lambda x : x[2])    
for i in range(N-1):
    B.append((abs(A[i][2]-A[i+1][2]),A[i][3],A[i+1][3]))

B.sort()

kruskal()

print(ans)