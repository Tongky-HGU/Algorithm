#복도뚫기
import sys
sys.setrecursionlimit(5000)

def find(a,vis):
    if vis[a] < 0:
        return a
    vis[a] = find(vis[a],vis)
    return vis[a]

def union(a,b,vis):
    a = find(a,vis)
    b = find(b,vis)

    if a == b:
        return False
    
    if(vis[a]  < vis[b]):
        vis[a] += vis[b];
        vis[b] = a;
    else:
        vis[b] += vis[a];
        vis[a] = b;

    return True

def solve():
    W = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    A = []
    B = []
    ans = W
    vis = [-1 for i in range(M+2)]

    for i in range(M):
        A.append(list(map(int,sys.stdin.readline().split())) + [i])

    for i in range(M):
        dist = A[i][0] - A[i][2]
        B.append((max(0,dist),i,M))

        dist = W - (A[i][0] + A[i][2])
        B.append((max(0,dist),i,M+1))

        for j in range(i):
            dist = ((A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2)**0.5 - A[i][2] - A[j][2]
            B.append((max(0,dist),i,j))

    B.sort()
    # print(B)

    for d,a,b in B:
        if union(a,b,vis):
            if find(M,vis) == find(M+1,vis):
                ans = min(d,ans)
                ans = print(round(ans/2,6))
                break



N = int(sys.stdin.readline())
for _ in range(N):
    solve()

