#통신망 분할
# 마지막을 음수로 갯수를 저장하는 기법
import sys
N, M, Q = map(int,sys.stdin.readline().split())
parent = [-1 for i in range(N+1)]
link = []
delete = []
notDelete = [1 for i in range(M+1)]
ans =0

def find(a):
    if parent[a] < 0 : return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b: return False
    parent[a] += parent[b]
    parent[b] = a
    return True

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    link.append([a,b])

for _ in range(Q):
    a = int(sys.stdin.readline())
    delete.append(a)
    notDelete[a] = 0

for i in range(1,len(notDelete)):
    if notDelete[i] :
        a,b = link[i-1]
        union(a,b)

delete.reverse()
for i in delete:
    a,b = link[i-1]
    temp = parent[find(a)]*parent[find(b)]
    if (union(a,b)): ans += temp
    # print(a,b,ans)
    # print(parent)

print(ans)