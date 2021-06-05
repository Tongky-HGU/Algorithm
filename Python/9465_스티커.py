# 스티커
import sys
T = int(sys.stdin.readline())

dr = [1,0,-1,0]
dc = [0,-1,0,1]


def solve():
    N = int(sys.stdin.readline())
    A = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0 for _ in range(N)] for _ in range(2)]
# dp 로저장
# 한칸 전 대각선 or 두 칸 전 중 큰수
    for i in range(N):
        if i == 0:
            dp[0][i], dp[1][i] = A[0][i], A[1][i]
        elif i == 1 :
            dp[0][i], dp[1][i] = A[0][i] + dp[1][i-1], A[1][i] + dp[0][i-1]
        else:
            dp[0][i] = max(dp[1][i-1],dp[0][i-2],dp[1][i-2]) + A[0][i]
            dp[1][i] = max(dp[0][i-1],dp[0][i-2],dp[1][i-2]) + A[1][i]
    
    print(max(dp[0][N-1],dp[1][N-1]))

for _ in range(T):
    solve()
