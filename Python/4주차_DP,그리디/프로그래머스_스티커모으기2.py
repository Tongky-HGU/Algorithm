def solution(sticker):
    ans = 0
    dp = [[0 for _ in range(len(sticker))] for _ in range(2)]
    
    if len(sticker) == 1: return sticker[0]
    
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    
    dp[1][0] = 0
    dp[1][1] = sticker[1]

    for i in range(2,len(sticker)):
        dp[0][i] = max(dp[0][i-1],dp[0][i-2]+sticker[i])
        dp[1][i] = max(dp[1][i-1],dp[1][i-2]+sticker[i])
        
    # print(dp)
    return max(dp[0][-2],dp[1][-1])