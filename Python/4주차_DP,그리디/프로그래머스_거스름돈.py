def solution(n, money):
    dp = [[0 for _ in range(n+1)] for _ in range(len(money)+1)]
    
    for i in range(len(money)+1):
        dp[i][0] = 1
        
    for i in range(n+1):
        for j in range(1,len(money)+1):
            if money[j-1] <= i:
                dp[j][i] = dp[j-1][i] + dp[j][i-money[j-1]]
            else:
                dp[j][i] = dp[j-1][i]
                
    return dp[-1][-1]