#별찍기 10
import sys
N = int(sys.stdin.readline())
A = [[" " for _ in range(N)] for _ in range(N)]

def dfs(x,y,n):
    if n == 1:
        A[x][y] = "*"
        return
    n = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            dfs(x+n*i,y+n*j,n)

dfs(0,0,N)

for i in range(N):
    print("".join(A[i]))