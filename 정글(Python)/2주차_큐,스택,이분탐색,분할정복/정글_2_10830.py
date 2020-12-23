# 행렬 곱셈
import sys

def matrix_exp(n,k):
    if k== 1:
        for i in range(N):
            for j in range(N):
                n[i][j] %= 1000
        return n

    elif (k % 2) >0:
        result = [[0]*N for _ in range(N)]
        m = matrix_exp(n,k-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += m[i][k] * n[k][j]
        for i in range(N):
            for j in range(N):
                result[i][j] %= 1000
        return result

    else:
        result = [[0]*N for _ in range(N)]
        m = matrix_exp(n,k//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += m[i][k] * m[k][j]
        for i in range(N):
            for j in range(N):
                result[i][j] %= 1000
        return result

N, K = map(int,sys.stdin.readline().split())

x = [[0]*N for _ in range(N)]
for i in range(N):
    x[i] = list(map(int,sys.stdin.readline().split()))

ans =matrix_exp(x,K)

for i in ans:
    for j in i:
        print(j, end = ' ')
    print()