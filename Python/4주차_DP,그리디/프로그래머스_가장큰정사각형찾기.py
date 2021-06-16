#가장큰정사각형찾기
def solution(board):
    ans = 0
    dp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]

    for i in range(1,len(board)+1):
        for j in range(1,len(board[0])+1):
            dp[i][j] = board[i-1][j-1]

    for i in range(1,len(board)+1):
        for j in range(1,len(board[0])+1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                ans = max(ans,dp[i][j])
                
    return ans*ans