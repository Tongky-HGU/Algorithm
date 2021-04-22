#친구 네트워크
import sys
def find(a):
    if a == parent[a]:
        return parent[a]
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a= find(a)
    b= find(b)
    if a==b:
        return
    parent[a]= b
    num[b] += num[a]

N = int(sys.stdin.readline())
for _ in range(N):
    M = int(sys.stdin.readline())
    parent= {}
    num = {}
    
    cnt = 0
    for _ in range(M):
        A ,B = sys.stdin.readline().split()
        for name in [A,B]:
            if name not in parent:
                parent[name]= name
                num[name]= 1
                cnt+=1
        union(A,B)
        # print(num[find(A)])
        ans = 0
        for name in parent:
            ans = max(ans,num[find(A)])
        print(ans)


    # print(parent)
