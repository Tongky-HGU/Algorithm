#플로이드
import sys,math
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
A = [[math.inf for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    A[a][b] = min(A[a][b],c)
# print(A)

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            A[i][j] = min(A[i][j],A[i][k]+A[k][j])
    
# print(A)

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j or A[i][j] == math.inf: 
            print(0,end=" ")
        else:
            print(A[i][j],end=" ")
    print("")