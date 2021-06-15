#합승택시요금
# 플로이드워셜 순서가 중요한지 몰랐다.
import math

def solution(n, s, a, b, fares):
    A = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        A[i][i] = 0

    for x,y,dist in fares:
        A[x][y] = dist
        A[y][x] = dist

    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                A[j][k] = min(A[j][k],A[j][i]+A[i][k])

    ans = math.inf

    for i in range(1,n+1):
        # print(A[s][i],A[i][a],A[i][b])
        ans = min(ans,A[s][i]+A[i][a]+A[i][b])
    
    return ans