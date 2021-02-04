#구간합배열5
import sys
N, M = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
B = [[0 for _ in range(N+1)] for _ in range(N+1)]

B[1][1] = A[0][0]
for i in range(1,N+1):
    for j in range(1,N+1):
        B[i][j] = A[i-1][j-1] + B[i][j-1] +B[i-1][j] - B[i-1][j-1]

# print(B);
for i in range(M):
    ans =0
    X1,Y1,X2,Y2 = map(int,sys.stdin.readline().split())
    ans =  B[X2][Y2] - B[X1-1][Y2] - B[X2][Y1-1] + B[X1-1][Y1-1]
    print(ans)


