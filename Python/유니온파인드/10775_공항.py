#공항
import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

gate = [i for i in range(G+1)]
plane = []
ans = 0

def find(a):
    if gate[a] == a:
        return a
    gate[a] = find(gate[a])
    return gate[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a == 0 and b == 0:
        return False
    gate[a] = b
    return True

for _ in range(P):
    plane.append(int(sys.stdin.readline()))

for p in plane:
    if (find(p)==0): break
    union(find(p),find(p)-1)
    ans+=1

    # if (union(find(p),find(p)-1)):
        # ans+=1
    # print(gate)
print(ans)
    
