#복도뚫기
import sys

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
    for d,a,b in B:
        if union(a,b):
            if find(M) == find(M+1) == find(a):
                ans = min(d,ans)


N = int(sys.stdin.readline())
for _ in range(N):
    W = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    A = []
    B = []
    ans = W
    vis = [i for i in range(M+2)]

    for i in range(M):
        A.append(list(map(int,sys.stdin.readline().split())) + [i])

    for i in range(M):
        temp = A[i][0] - A[i][2]
        if temp > 0:
            B.append((temp,i,M))
        else:
            B.append((0,i,M))

        temp = W - (A[i][0] + A[i][2])
        if temp > 0:  
            B.append((temp,i,M+1))
        else:
            B.append((0,i,M+1))

        for j in range(i+1,M):
            temp = ((A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2)**0.5 - A[i][2] - A[j][2]
            if temp > 0:
                B.append((temp,i,j))
            else:
                B.append((0,i,j))

    B.sort()
    kruskal()

    ans = print(round(ans/2,6))
