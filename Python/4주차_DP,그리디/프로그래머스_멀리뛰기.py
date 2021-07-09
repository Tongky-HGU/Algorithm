# 멀리 뛰기
def solution(n):
    if n < 3: return n
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)        
    return dp[n] %1234567

print(solution(4))