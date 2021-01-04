#행렬 곱셈 순서
import sys, math
N = int(sys.stdin.readline())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(1,N): # 대각선 위에서 내려옴  size 얼마나 자를건지 
    for j in range(N-i): # 모든 행렬에 대해서 수행 
        dp[j][j+i] = math.inf # 커서의 오른쪽에 inf를 미리 넣어줌
        for k in range(j,j+i): #자를 수 있는 경우의 수를 모두 
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + A[j][0]*A[k][1]*A[j+i][1])
            # for x in range(N):
            #     print(*dp[x])
            # print(f"i ={i} j ={j} k = {k}" +"*"*24)
            # print(f"{dp[j][k]}+{dp[k+1][j+i]}+ {A[j][0]}*{A[k][1]}*{A[j+i][1]}" +"*"*24)
print(dp[0][N-1])


        